# pywin32(win32com)のライブラリを読み込み
import win32com.client as com
import os

# 保存先は絶対パスで絶対パスで指定する必要がある
scr_file = os.path.abspath(__file__)
scr_dir = os.path.dirname(scr_file)
save_file = scr_dir + "/pywin32save.xlsx"

# Excelの起動
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelに新規ワークブックを追加
book = app.Workbooks.Add()
# アクティブなシートを得る
sheet = book.ActiveSheet

# シートに値を書き込む
sheet.Range("A1").Value = "あ"
sheet.Range("B2").Value = "い"
sheet.Range("C3").Value = "う"

# ブックを保存
book.SaveAs(save_file)
# Excelを終了
app.Quit()
