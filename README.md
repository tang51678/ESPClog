# ESPClog

1. **导入库**：脚本导入了 `pandas` 和 `streamlit`，这是进行数据分析和创建交互式应用的常见组合。
2. **`load_and_filter_data` 函数**：这个函数负责读取 Excel 文件，并根据提供的筛选条件过滤数据。它还执行了一些数据聚合操作，比如计算每个源地址的事件次数，并合并了相关的数据。
3. **`main` 函数**：这是 Streamlit 应用的入口点。它允许用户上传一个 Excel 文件，并提供了一些输入框和按钮来配置筛选条件。当用户点击“开始分析”按钮时，它会调用 `load_and_filter_data` 函数并显示结果。
4. **用户界面**：脚本使用 Streamlit 的组件来创建一个简单的用户界面，包括标题、文件上传器、文本输入框、多选框、数字输入框和按钮。
5. **数据显示**：脚本使用 `st.write` 和 `unsafe_allow_html=True` 来显示带有 HTML 标签的文本，以便对事件次数进行着色。



# 使用方法：

python3 写的

pip install -r requirement.txt

streamlit run 3.1.py     
![image](https://github.com/tang51678/ESPClog/assets/80816552/e95bf319-5eb6-429d-b3fe-5d86e13393d8)
![image](https://github.com/tang51678/ESPClog/assets/80816552/e6c410d4-33a3-4cca-85a6-5c9a42c01034)

# 更新日志！



- v 1
- v2
- v3
- v3.1  更新时间: 2024-05-22 还在不断优化中 大师傅勿喷！！！
- v3.2  更新时间: 2024-06-08 优化了奇怪报错！！！

## 如果能帮到你解决问题，点个start吧！！！
