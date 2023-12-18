import openpyxl as excel

# 新規ワークブックを作成
book = excel.Workbook()

# アクティブなワークシートを取得
sheet = book.active

# A1のセル値を設定
sheet["A1"] = "Asobo"
book.save("Asobo.xlsx")
