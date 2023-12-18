import win32com.client as com
import os

# ファイルは絶対パスで指定する必要がある
scr_file = os.path.abspath(__file__)

scr_dir = os.path.dirname(scr_file)
in_file = scr_dir + "/pywin32save.xlsx"
pdf_file = scr_dir + "/pywin32save.pdf"

# Excelの起動
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelでブックを読み込み
try:
    book = app.Workbooks.Open(in_file)
    # ブックをPDFでエクスボート
    xlTYPEPDF = 0  # PDFを表す定数
    book.ExportAsFixedFormat(xlTYPEPDF, pdf_file)  # PDFファイル名を指定
except:
    print("エラー")
finally:
    # Excelを終了させる
    app.Quit()
    print("正しく終了")
