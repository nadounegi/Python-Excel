import openpyxl as excel

book = excel.load_workbook("Style.xlsx")
sheet = book.active

cell = sheet["d2"]
cell.value = "文字"

from openpyxl.styles.alignment import Alignment

cell.alignment = Alignment(horizontal="center", vertical="center")
book.save("Style.xlsx")
