import openpyxl
from openpyxl.formatting.rule import DataBarRule

fname = "第五回/5_tikan.xlsx"
wb = openpyxl.load_workbook(fname)
ws = wb.active
nrule = DataBarRule(
    start_type="num",
    start_value=0,
    end_type="num",
    end_value=50,
    color="00FFFF",
    minLength=0,
    maxLength=100,
)
ws.conditional_formatting.add("c4:c10", nrule)
wb.save(fname)
