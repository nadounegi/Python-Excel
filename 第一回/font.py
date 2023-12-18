import openpyxl as excel


book = excel.Workbook()
sheet = book.active

cell = sheet["B2"]
cell.value = "Asobo"
from openpyxl.styles import Font

cell.font = Font(color="FF00FF")
cell.font = Font(size=20, bold=True, italic=True, color="FF0000")
book.save("Style.xlsx")
