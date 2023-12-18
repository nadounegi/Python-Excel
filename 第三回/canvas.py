import tkinter

root = tkinter.Tk()
root.title("初めての画像表示")
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()
gazou = tkinter.PhotoImage(file="GL4.gif")
canvas.create_image(200, 300, image=gazou)
root.mainloop()
