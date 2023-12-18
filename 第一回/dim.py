import openpyxl as excel

book = excel.load_workbook("style.xlsx")
sheet = book.active

cell = sheet["c2"]
cell.value = "皆遊ぼう"

sheet.column_dimensions["c"].width = 40
sheet.row_dimensions[2].height = 40

book.save("style.xlsx")
