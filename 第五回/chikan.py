import openpyxl

# 5_tikan.xlsxの開発を企画に置換する
fname = "第五回/5_tikan.xlsx"
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows():
    for cel in row:
        s = str(cel.value)
        if "開発" in s:
            cel.value = s.replace("開発", "企画")
wb.save(fname)
