import random
import tkinter.messagebox

cnt = 0
while True:
    r = random.randint(1, 10)
    print(r)
    cnt += 1
    if r == 7:
        break
tkinter.messagebox.showinfo("情報", str(cnt) + "回目で7ゲット")
