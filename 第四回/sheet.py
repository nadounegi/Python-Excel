import openpyxl as excel

# 新規ブックを作成
book = excel.Workbook()
book.active["B2"] = "OK"

# 繰り返し5回シートを作成する
for i in range(1, 5):
    # シートを作成
    sname = "No" + str(i)
    sheet = book.create_sheet(title=sname)
# 1番をコピー
s1 = book.copy_worksheet(book["No1"])
# シート名の変更
s1.title = "No1のコピー"
# シートの削除
book.remove(book["No1"])
# ファイルの保存
book.save("2_sheet.xlsx")
