import pandas as pd
import streamlit as st
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def load_data(file_name):
    """Load data from an Excel file."""
    return pd.read_excel(file_name, engine='openpyxl')


def filter_data(df, service_type, risk_levels, min_event_count):
    """Filter the DataFrame based on the given criteria."""
    filtered_df = df[
        (df['目的地址'].str.contains('192.168.168')) &
        (df['服务类型'].str.contains(service_type, regex=True)) &
        (df['危险程度'].isin(risk_levels)) &
        (df['事件次数'] >= min_event_count)
        ]
    return filtered_df


def aggregate_data(filtered_df):
    """Aggregate data by source address."""
    address_count = filtered_df.groupby('源地址')['事件次数'].sum().reset_index()
    address_destinations = filtered_df.groupby('源地址')['目的地址'].unique().apply(
        lambda x: ', '.join(set(x))).reset_index()
    address_events = filtered_df.groupby('源地址')['事件名称'].unique().apply(
        lambda x: ', '.join(set(x))).reset_index()

    # Merge data
    address_count = address_count.merge(address_events, on='源地址', how='left')
    address_count = address_count.merge(address_destinations, on='源地址', how='left')

    return address_count


def main():
    st.title('上传并分析Excel文件')

    # Allow users to upload a file
    uploaded_file = st.file_uploader('选择要分析的Excel文件', type='xlsx')

    if uploaded_file is not None:
        # Load the data from the file
        df = load_data(uploaded_file)

        # Provide filters for the user
        service_type = st.text_input('服务类型 (使用正则表达式)', 'www|FTP|SSH')
        risk_levels = st.multiselect('危险程度', ['低风险', '中风险', '高风险'], default=['中风险', '高风险'])
        min_event_count = st.number_input('最小事件次数', value=50)

        if st.button('开始分析'):
            # Apply filters
            try:
                filtered_df = filter_data(df, service_type, risk_levels, min_event_count)
                aggregated_data = aggregate_data(filtered_df)

                # Display the aggregated data
                st.write(aggregated_data)

            except KeyError as e:
                st.error(f"错误：找不到列 '{e.args[0]}'。请检查你的数据文件和筛选条件。")


if __name__ == "__main__":
    main()
