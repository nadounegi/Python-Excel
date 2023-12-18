import openpyxl
from openpyxl.chart import BarChart, Reference, Series

# ワークブックを作成
wb = openpyxl.Workbook()
ws = wb.active

for i in range(10):
    ws.append([i])

# グラフ範囲の指定
values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)
# 系列名の指定
s = Series(values, title="keiretumei")
# グラフは棒グラフ
chart = BarChart()
# グラフタイトル指定
chart.title = "title"
# グラフに系列を追加
chart.append(s)

# chart add_data(values)
ws.add_chart(chart, "E5")
wb.save("2_Chart.xlsx")
