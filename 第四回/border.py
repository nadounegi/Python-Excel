import openpyxl as excel

book = excel.Workbook()
sheet = book.active

# 罫線の指定
from openpyxl.styles.borders import Border, Side

border1 = Border(
    top=Side(style="thin", color="000000"),
    bottom=Side(style="thin", color="000000"),
    left=Side(style="thin", color="000000"),
    right=Side(style="thin", color="000000"),
)
border2 = Border(
    top=Side(style="double", color="ff0000"),
    bottom=Side(style="double", color="00ff00"),
    left=Side(style="double", color="0000ff"),
    right=Side(style="double", color="00ffff"),
)
border3 = Border(
    top=Side(style="thin", color="000000"),
    bottom=Side(style="double", color="000000"),
    left=Side(style="thin", color="000000"),
    right=Side(style="thin", color="000000"),
)
# セルに罫線を設定　細い罫線を全体に
for rows in sheet["b2":"f6"]:
    for cell in rows:
        cell.border = border1
# いろいろな線を複数セルに
for rows in sheet["b2":"f6"]:
    for cell in rows:
        cell.border = border1
# いろいろな線を複数セルに
for rows in sheet["c10":"g15"]:
    for cell in rows:
        cell.border = border2
# 最初の罫線の１行目の下でけ２重罫線
for rows in sheet["b2":"f2"]:
    for cell in rows:
        cell.border = border3
book.save("border.xlsx")
