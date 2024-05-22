import warnings
import pandas as pd


def load_and_filter_data(file_name, service_type, risk_levels, min_event_count):
    # 解决告警
    warnings.filterwarnings('ignore')

    # 读取 Excel 文件并指定使用 OpenPyXL 引擎
    df = pd.read_excel(file_name, engine='openpyxl')

    # 筛选条件
    filtered_df = df[(df['目的地址'].str.contains('192.168.168')) &
                     (df['服务类型'].str.contains(service_type, regex=True)) &
                     (df['危险程度'].isin(risk_levels)) &
                     (df['事件次数'] >= min_event_count)]

    # 统计每个源地址的事件次数
    address_count = filtered_df.groupby('源地址')['事件次数'].sum().reset_index()

    # 获取每个源地址对应的目的地址列表（去重）
    address_destinations = filtered_df.groupby('源地址')['目的地址'].unique().apply(
        lambda x: ', '.join(set(x))).reset_index()

    # 获取每个源地址对应的事件名称
    address_events = filtered_df.groupby('源地址')['事件名称'].unique().apply(lambda x: ', '.join(set(x))).reset_index()

    # 合并事件次数和事件名称
    address_count = address_count.merge(address_events, on='源地址', how='left')

    # 合并事件次数和目的地址列表
    address_count = address_count.merge(address_destinations, on='源地址', how='left')

    return address_count


def print_address_event_counts(address_count):
    # 输出结果
    for index, row in address_count.iterrows():
        print(
            f"{row['源地址']} 源地址--对应有 {row['事件次数']} 条事件--相对应的目的地址是: {row['目的地址']}--相对应这些事件名称有：{row['事件名称']}")


# 使用示例
file_name = './政务易waf日志20240521_17点30分~20240522_9点.xlsx'
service_type = 'www|FTP|SSH'
risk_levels = ['中风险', '高风险', '低风险']
min_event_count = 50

address_count = load_and_filter_data(file_name, service_type, risk_levels, min_event_count)
print_address_event_counts(address_count)
