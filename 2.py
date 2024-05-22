import warnings
warnings.filterwarnings('ignore')   #解决告警

import pandas as pd
# 读取 Excel 文件并指定使用 OpenPyXL 引擎
df = pd.read_excel('ipslog_1715937027.xlsx', engine='openpyxl')

# 筛选条件
filtered_df = df[(df['目的地址'].str.contains('192.168.168')) &
                 (df['服务类型'] == 'www') &
                 (df['危险程度'].isin(['中风险', '高风险'])) &
                 (df['事件次数'] >= 50)]

# 统计每个源地址的事件次数
address_count = filtered_df.groupby('源地址')['事件次数'].sum().reset_index()

# 输出结果
for index, row in address_count.iterrows():
    print(f"{row['源地址']} 源地址对应有 {row['事件次数']} 条事件")
