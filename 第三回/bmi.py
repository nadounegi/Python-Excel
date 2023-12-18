import tkinter

def standard_weight(height):
    return int((height - 100) * 0.9)

def bmi():
    height_value = float(height.get())
    weight_value = float(weight.get())
    bmi_value = weight_value / (height_value / 100) ** 2
    return round(bmi_value, 1)

def calculate_bmi():
    bmi_value = bmi()
    if bmi_value is not None:
        result_label.config(text=f"BMIは{bmi_value}です。")

def hyoka_bmi():
    bmi_value = bmi()
    if bmi_value is not None:
        if bmi_value >= 25:
            result_label.config(text="肥満")
        elif bmi_value < 18:
            result_label.config(text="やせすぎ")

def calculate_standard_weight():
    height_value = float(height.get())
    standard_weight_value = standard_weight(height_value)
    result_label.config(text=f"標準体重は{standard_weight_value}kgです。")

root = tkinter.Tk()
root.title("BMI")
root.geometry("400x250")

# 身長の入力欄
height = tkinter.Entry(width=5)
height.place(x=10, y=10)
height_label = tkinter.Label(text="cm")
height_label.place(x=70, y=10)

# 体重の入力欄
weight = tkinter.Entry(width=5)
weight.place(x=10, y=60)
weight_label = tkinter.Label(text="kg")
weight_label.place(x=70, y=60)

# 結果表示のラベル
result_label = tkinter.Label(text="", bg="white", width=40, height=2)
result_label.place(x=10, y=190)

# BMIの計算
button = tkinter.Button(text="BMI", command=calculate_bmi)
button.place(x=10, y=110)

# 評価
button = tkinter.Button(text="BMI評価", command=hyoka_bmi)
button.place(x=10, y=135)

# 標準体重の計算
button = tkinter.Button(text="標準体重", command=calculate_standard_weight)
button.place(x=10, y=160)

root.mainloop()
