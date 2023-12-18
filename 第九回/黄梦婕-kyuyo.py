from asyncio.windows_events import INFINITE
from cProfile import label
from logging import root
import symtable
import tkinter as tk
import openpyxl as excel


def show_selected(event):
    global selected_sya

    selection = lb.curselection()
    if selection:
        index = selection[0]
        syas = ["相沢　沙希", "生田　真一", "井川　春子", "木村　かえ", "近藤　春香"]
        selected_sya = syas[index]


def get_selected_sya():
    return selected_sya


def sya_no():
    syas = ["相沢　沙希", "生田　真一", "井川　春子", "木村　かえ", "近藤　春香"]
    for i in range(len(syas)):
        if syas[i] == selected_sya:
            sya_no = 100 + int(i)
            i += 1
            return sya_no


def caculate_salary():
    # 時間内給与
    base_slary = hw.get() * wh.get()
    # 残業給与
    over_time_salary = hw.get() * oh.get() * 1.2
    # 給与合計
    total_salary = base_slary + over_time_salary

    return base_slary, over_time_salary, total_salary


def click_btn():
    book = excel.load_workbook("第九回/kyuyo.xlsx")
    sheet_sya = get_selected_sya()

    if sheet_sya:
        selectedsheet = book[sheet_sya]
        default_sheet = book["給与一覧"]

        # 開始行を取得
        min_row = 3
        while selectedsheet.cell(row=min_row, column=1).value != None:
            min_row += 1

        default_min_row = 3
        while default_sheet.cell(row=default_min_row, column=1).value != None:
            default_min_row += 1

        # データを書き込む
        selectedsheet.cell(row=min_row, column=1).value = hw.get()
        default_sheet.cell(row=default_min_row, column=1).value = hw.get()
        selectedsheet.cell(row=min_row, column=2).value = wd.get()
        default_sheet.cell(row=default_min_row, column=2).value = wd.get()
        selectedsheet.cell(row=min_row, column=3).value = wh.get()
        default_sheet.cell(row=default_min_row, column=3).value = wh.get()
        selectedsheet.cell(row=min_row, column=4).value = oh.get()
        default_sheet.cell(row=default_min_row, column=4).value = oh.get()

        # Excelファイルを保存
        book.save("第九回/kyuyo.xlsx")


root = tk.Tk()
root.title("給与計算")
#   画面サイズ
root.geometry("700x700")

# 社員リスト
sl_lb = tk.Label(root, text="社員リスト", font=("New Times Roman", 12, "bold"))
sl_lb.place(x=235, y=20)

# 社員リストボックス
sya_list = tk.StringVar()
sya_list.set(["相沢　沙希", "生田　真一", "井川　春子", "木村　かえ", "近藤　春香"])
lb = tk.Listbox(root, height=5, listvariable=sya_list, selectmode="single")
lb.place(x=350, y=20)
lb.bind("<<ListboxSelect>>", show_selected)

# 勤務日入力欄
wd_lb = tk.Label(root, text="勤務日", font=("New Times Roman", 12, "bold"))
wd_lb.place(x=220, y=300)
wd = tk.Entry(width=15)
wd.place(x=280, y=300)

# 勤務時間入力欄
wh_lb = tk.Label(root, text="勤務時間", font=("New Times Roman", 12, "bold"))
wh_lb.place(x=200, y=340)
wh = tk.Entry(width=15)
wh.place(x=280, y=340)

# 残業時間入力欄
oh_lb = tk.Label(root, text="残業時間", font=("New Times Roman", 12, "bold"))
oh_lb.place(x=200, y=380)
oh = tk.Entry(width=15)
oh.place(x=280, y=380)

# 入力ボタン
btn = tk.Button(root, text="入力", font=("New Times Roman", 12, "bold"))
# ボタンの位置を指定
btn.place(x=280, y=450)
root.mainloop()
