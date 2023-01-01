from tkinter import *

root = Tk()
root.title("Welcome to Simple Calculator")

inp = Entry(root,width=50, borderwidth=3)
inp.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    #inp.delete(0, END)
    crr = inp.get()
    inp.delete(0, END)
    inp.insert(0, str(crr) + str(number))


def button_clear():
    inp.delete(0, END)


def button_add():
    first = inp.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first)
    inp.delete(0, END)


def button_sub():
    first = inp.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first)
    inp.delete(0, END)
    return


def button_mul():
    first = inp.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first)
    inp.delete(0, END)
    return


def button_div():
    first = inp.get()
    global f_num
    global math
    math = "division"
    f_num = int(first)
    inp.delete(0, END)
    return


def button_equal():
    second = inp.get()
    inp.delete(0, END)

    if math == "addition":
        inp.insert(0, int(second)+f_num)

    elif math == "subtraction":
        inp.insert(0, int(second) - f_num)

    elif math == "multiplication":
        inp.insert(0, int(second) * f_num)

    elif math == "division":
        inp.insert(0, int(second) / f_num)
        

bt1 = Button(root, text="1", padx=50, pady=40, command=lambda: button_click(1))
bt2 = Button(root, text="2", padx=50, pady=40, command=lambda: button_click(2))
bt3 = Button(root, text="3", padx=50, pady=40, command=lambda: button_click(3))
bt4 = Button(root, text="4", padx=50, pady=40, command=lambda: button_click(4))
bt5 = Button(root, text="5", padx=50, pady=40, command=lambda: button_click(5))
bt6 = Button(root, text="6", padx=50, pady=40, command=lambda: button_click(6))
bt7 = Button(root, text="7", padx=50, pady=40, command=lambda: button_click(7))
bt8 = Button(root, text="8", padx=50, pady=40, command=lambda: button_click(8))
bt9 = Button(root, text="9", padx=50, pady=40, command=lambda: button_click(9))
bt0 = Button(root, text="0", padx=50, pady=40, command=lambda: button_click(0))
bt_add = Button(root, text="+", padx=49, pady=40, command=lambda: button_add())
bt_sub = Button(root, text="-", padx=51, pady=40, command=lambda: button_sub())
bt_mul = Button(root, text="x", padx=51, pady=40, command=lambda: button_mul())
bt_div = Button(root, text="/", padx=51, pady=40, command=lambda: button_div())
bt_equal = Button(root, text="=", padx=110, pady=40, command=lambda: button_equal())
bt_clear = Button(root, text="Clear", padx=100, pady=40, command=lambda: button_clear())

bt1.grid(row=3, column=0)
bt2.grid(row=3, column=1)
bt3.grid(row=3, column=2)

bt4.grid(row=2, column=0)
bt5.grid(row=2, column=1)
bt6.grid(row=2, column=2)

bt7.grid(row=1, column=0)
bt8.grid(row=1, column=1)
bt9.grid(row=1, column=2)

bt0.grid(row=4, column=0)
bt_clear.grid(row=4, column=1, columnspan=2)
bt_add.grid(row=5, column=0)
bt_equal.grid(row=5, column=1, columnspan=2)

bt_sub.grid(row=6,column=0)
bt_mul.grid(row=6,column=1)
bt_div.grid(row=6,column=2)
root.mainloop()