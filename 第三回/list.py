import tkinter
import tkinter.messagebox


def click_btn():
    # list
    n = lb.curselection()  # 選択されている項目のインデックスを取得
    # print(lb.get(n))  #選択されている項目の値を取得
    pno = lb.get(n)
    tkinter.messagebox.showinfo("確認", pno)


root = tkinter.Tk()
root.title("meibo")
root.geometry("400x400")

# リスト作成
list_value = tkinter.StringVar()
list_value.set(["学生", "会社員", "主婦"])
lb = tkinter.Listbox(height=3, listvariable=list_value, selectmode="single")
lb.place(x=10, y=180)

label1 = tkinter.Label(root, text="職業")
label1.place(x=10, y=150)

button = tkinter.Button(
    root, text="入力", font=("Times New Roman", 18), command=click_btn
)
button.place(x=200, y=300)

root.mainloop()  # 画面を表示
