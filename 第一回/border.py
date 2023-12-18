from turtle import color
import openpyxl as excel

book = excel.Workbook()
sheet = book.active

cell = sheet["e2"]
cell.value = "边框"

from openpyxl.styles.borders import Border, Side

cell.border = Border(
    top=Side(style="double", color="FF0000"),
    right=Side(style="thick", color="00FF00"),
    left=Side(style="dotted", color="ed7d31"),
    bottom=Side(style="dashDot", color="ad7d31"),
)

book.save("border.xlsx")
