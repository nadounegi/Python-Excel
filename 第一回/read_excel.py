import openpyxl as excel

# ワークブック(Excelファイル)を開く
book = excel.load_workbook("Asobo.xlsx")

# 先頭のワークシートの取り出し
sheet = book.worksheets[0]

# A1のセル値を取得
cell = sheet["A1"]

print(cell.value)
