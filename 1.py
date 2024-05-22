import warnings
import pandas as pd


def load_and_filter_data(file_name, service_type, risk_levels, min_event_count):
    # 解决告警
    warnings.filterwarnings('ignore')

    # 读取 Excel 文件并指定使用 OpenPyXL 引擎
    df = pd.read_excel(file_name, engine='openpyxl')

    # 筛选条件
    filtered_df = df[(df['服务类型'] == service_type) &
                     (df['危险程度'].isin(risk_levels)) &
                     (df['事件次数'] >= min_event_count)]

    # 统计每个源地址的事件次数
    address_count = filtered_df.groupby('源地址')['事件次数'].sum().reset_index()

    # 获取每个源地址对应的事件名称
    address_events = filtered_df.groupby('源地址')['事件名称'].unique().apply(lambda x: ', '.join(set(x))).reset_index()

    # 合并事件次数和事件名称
    address_count = address_count.merge(address_events, on='源地址', how='left')

    return address_count


def print_address_event_counts(address_count):
    # 输出结果
    for index, row in address_count.iterrows():
        print(f"{row['源地址']} 源地址对应有 {row['事件次数']} 条事件 对应这些事件名称有：{row['事件名称']}")


# 使用示例
file_name = 'ipslog_1715937027.xlsx'
service_type = 'www'
risk_levels = ['中风险', '高风险']
min_event_count = 50

address_count = load_and_filter_data(file_name, service_type, risk_levels, min_event_count)
print_address_event_counts(address_count)
