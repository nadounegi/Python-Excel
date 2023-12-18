from ctypes import wstring_at
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

fname = "第五回/5_tikan.xlsx"
wb = openpyxl.load_workbook(fname)
ws = wb.active
dv = DataValidation(type="whole", operator="between", formula1=18, formula2=70)
dv.errorTitle = "年齢の問題"
dv.error = "18~70までです"
dv.promptTitle = "年齢の入力"
dv.prompt = "年齢を入力してください。"
dv.add("c4:c10")
ws.add_data_validation(dv)
wb.save(fname)
