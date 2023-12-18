import openpyxl as excel

# ワークブックを開いてシートを得る
book = excel.load_workbook("第二回/test100.xlsx")
# アクティブなワークシアクティブを取得
sheet = book.active

# 連続でセルの値を得て表示
for y in range(2, 5):
    r = []
    for x in range(2, 5):
        v = sheet.cell(row=y, column=x).value
        r.append(v)
    print(r)
