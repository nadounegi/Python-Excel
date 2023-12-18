from logging import root
import tkinter
import tkinter.messagebox as msg


def click_btn():
    # radio
    text_check = var.get()
    if text_check == 0:
        msg.showinfo("確認", "男性")
    elif text_check == 1:
        msg.showinfo("確認", "女性")
    else:
        msg.showinfo("確認", "チェックされていません")


root = tkinter.Tk()
root.title("meibo")
root.geometry("400x400")
# int型の値を入れる
var = tkinter.IntVar()
radio1 = tkinter.Radiobutton(text="男性", variable=var, value=0)
radio1.place(x=10, y=50)

radio2 = tkinter.Radiobutton(text="女性", variable=var, value=1)
radio2.place(x=70, y=50)

button = tkinter.Button(
    root, text="入力", font=("Times New Roman", 18), command=click_btn
)
button.place(x=200, y=300)
root.mainloop()  # 画面を表示
