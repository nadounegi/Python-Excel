import tkinter
import openpyxl as exc
from datetime import datetime


def show_selected(event):
    # 获取当前选中项的索引
    index = tkinter.lb.curselection()[0]  # 注意这里直接使用lb变量
    # 构建文件名
    fname = "ice" + str(index + 1) + ".gif"
    # 加载图片
    gazou2 = tkinter.PhotoImage(file=fname)
    # 在画布上显示图片，注意使用canvas变量
    tkinter.canvas.create_image(205, 100, image=gazou2)
    # 调用显示价格等信息的函数
    hyoji()


def check():
    global topsu
    global gazou3

    for i in range(4):
        if tkinter.bvar[i].get() == False:
            if i == 0:
                gazou3 = tkinter.PhotoImage(file="")
                tkinter.canvas.create_image(205, 100, image="")
        else:
            if i == 0:
                gazou3 = tkinter.PhotoImage(file="")
                tkinter.canvas.create_image(205, 100, image="")
                topsu = topsu + 1
        hyoji()

    # 値段などを表示する関数


def hyoji():
    list_value = tkinter.StringVar()
    list_value.set(["ストロベリー　300円", "バニラ　350円", "抹茶　400円", "チョコレート　450円", "チーズケーキ　500円"])
    tkinter.lb = tkinter.Listbox(height=4, listvariable=list_value, selectmode="single")
    tkinter.lb.place(x=400, y=350)
    tkinter.lb.bind("<<ListboxSelect>>", show_selected)

    # 値段表示
    if topsu == 0:
        tkinter.Label(text="値段：300円", font=("Times New Roman", 18)).place(x=400, y=450)
    elif topsu == 1:
        tkinter.Label(text="値段：350円", font=("Times New Roman", 18)).place(x=400, y=450)
    elif topsu == 2:
        tkinter.Label(text="値段：400円", font=("Times New Roman", 18)).place(x=400, y=450)
    elif topsu == 3:
        tkinter.Label(text="値段：450円", font=("Times New Roman", 18)).place(x=400, y=450)
    elif topsu == 4:
        tkinter.Label(text="値段：500円", font=("Times New Roman", 18)).place(x=400, y=450)

    # トッピング料金表示
