import tkinter as tk
import random


def judge_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "引き分け！"
    elif (
        (player_choice == 2 and computer_choice == 0)
        or (player_choice == 0 and computer_choice == 1)
        or (player_choice == 1 and computer_choice == 2)
    ):
        return "優勝！"
    else:
        return "負けだ。。。"


def show_selected(event):
    global gazou1_1, n
    n = lb.curselection()
    if n[0] == 0:
        fname = "第六回\images\Gu1.gif"
    elif n[0] == 1:
        fname = "第六回\images\Choki1.gif"
    else:
        fname = "第六回\images\Pa1.gif"

    gazou1_1 = tk.PhotoImage(file=fname)
    canvas.create_image(205, 300, image=gazou1_1)


def click_btn():
    global n, r1, gazou2_1, gazou3_1
    r1 = random.randint(0, 2)
    if r1 == 0:
        fname2 = "第六回\images\Gu2.gif"
    elif r1 == 1:
        fname2 = "第六回\images\Choki2.gif"
    else:
        fname2 = "第六回\images\Pa2.gif"
    gazou2_1 = tk.PhotoImage(file=fname2)
    canvas.create_image(205, 100, image=gazou2_1)
    result = judge_winner(n[0], r1)
    result_label.config(text=result)


root = tk.Tk()
root.title("じゃんけんゲーム")
root.resizable(False, False)
canvas = tk.Canvas(root, width=700, height=500)
canvas.pack()

# 初期化画像变量
gazou2_1 = tk.PhotoImage(file="")
canvas.create_image(205, 100, image=gazou2_1)
gazou1_1 = tk.PhotoImage(file="")
canvas.create_image(205, 300, image=gazou1_1)

# 结果レベル
result_label = tk.Label(root, text="", font=("Times New Roman", 18))
result_label.place(x=200, y=450)

# 创建リスト
list_value = tk.StringVar()
list_value.set(["ぐー", "チョキ", "パー"])
lb = tk.Listbox(height=3, listvariable=list_value, selectmode="single")
lb.place(x=400, y=350)
lb.bind("<<ListboxSelect>>", show_selected)

# ボタン作成
button = tk.Button(root, text="じゃんけん", font=("Times New Roman", 18), command=click_btn)
button.place(x=200, y=200)

root.mainloop()
