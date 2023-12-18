import tkinter
import tkinter.messagebox


def check():
    if cval.get() == True:
        tkinter.messagebox.showinfo("確認", "チェックされています")
    else:
        tkinter.messagebox.showinfo("確認", "チェックされていません")


root = tkinter.Tk()
root.title("チェックの状態を知る")
root.geometry("400x200")
root.geometry("400x200")
# #チェックされているかどうか調べる
cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text="チェックボタン", variable=cval, command=check)
cbtn.pack()
root.mainloop()
