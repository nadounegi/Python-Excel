import tkinter

root = tkinter.Tk()
root.title("初めてウインドウ")
root.geometry("800x600")
# サイズ変更不可
root.resizable(False, False)

# ラベル作成
label = tkinter.Label(root, text="ラベル", font=("Times New Roman", 20), bg="white")
# 放置位置の指定
label.place(x=300, y=60)

# ボタン作成
button = tkinter.Button(root, text="ボタン", font=("Times New Roman", 20), fg="skyblue")
# 放置位置の指定
button.place(x=360, y=400)

# テキストボックス
entry = tkinter.Entry(width=20)
# 放置位置の指定,指定したくない場合は、entry.pack()を使う
entry.place(x=10, y=10)

root.mainloop()
