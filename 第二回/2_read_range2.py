import openpyxl as excel

# ワークブックを開いてシートを取り出す
book = excel.load_workbook("第二回/test100.xlsx")
sheet = book.active

# 連続でセルの値を得る
for row in sheet["B2":"D4"]:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)
