import openpyxl as excel
from datetime import datetime

# 現在時刻を取得して任意の書式で表示
t = datetime.now()
# 新規ワークブックを作成
wb = excel.Workbook()

# アクティブなワークシートを取得
sheet = wb.active
# 日付を和暦
sheet["B5"] = t
sheet["B5"].number_format = '[$-ja-JP]ggge"年"m"月"d"日"'
sheet.column_dimensions["B"].width = 20

# 日付を西暦
sheet["B6"] = t
sheet["B6"].number_format = 'yyyy"年"m"月"d"日"'

# 数値を桁区切り
sheet["d5"] = 10000
sheet["d5"].number_format = "#,##0.00"

# 数値を通貨
sheet["d6"] = 10000
sheet["d6"].number_format = "¥#,##0;[red]¥-#,##0"

# 足し算
sheet["d7"] = "=d5+d6"
# sum関数
sheet["d8"] = "=sum(d5:d6)"
# ファイルを保存
wb.save("第二回/1_format.xlsx")
wb.save("第二回/num.xlsx")
