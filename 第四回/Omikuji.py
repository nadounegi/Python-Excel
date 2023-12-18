import tkinter as tk
import random

# おみくじの結果リスト
fortunes = ["大吉", "中吉", "小吉", "吉", "凶"]


def draw_fortune():
    # おみくじの結果をランダムに選ぶ
    result = random.choice(fortunes)
    # ラベルに結果を表示
    result_label.config(text=result)


# ウィンドウの作成
root = tk.Tk()
root.title("おみくじゲーム")

# ボタンの作成と配置
btn = tk.Button(root, text="おみくじを引く", command=draw_fortune)
btn.pack(pady=20)

# 結果を表示するラベルの作成と配置
result_label = tk.Label(root, text="", font=("Arial", 24), bg="white")
result_label.pack(pady=20)

# ウインドウの大きさ
root.geometry("400x300")

root.mainloop()
