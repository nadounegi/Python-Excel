import openpyxl as excel

# 新規ワークブックを作成
wb = excel.Workbook()
# アクティブなワークシアクティブを取得
sheet = wb.active
# 連続でセルに値を設定する
for i in range(10):
    # セルに値を設定
    sheet.cell(row=(i + 1), column=1, value=i)
# ファイルを保存
wb.save("第二回/2_renzoku.xlsx")
