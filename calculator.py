from tkinter import *
import tkinter.messagebox
import math

# creating main window
root = Tk()
root.title("Simple Calculator")
root.config(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("468x540+0+0")


# funcions of buttons
def button_click(number):
    current = display_scr.get()
    display_scr.delete(0, END)
    display_scr.insert(0, str(current) + str(number))


def button_clear():
    display_scr.delete(len(display_scr.get()) - 1, END)


def button_clearAll():
    display_scr.delete(0, END)


def evaluate_expression():
    result = eval(display_scr.get())
    display_scr.delete(0, END)
    display_scr.insert(0, result)


def mathPM():
    current = -(float(display_scr.get()))
    display_scr.delete(0, END)
    display_scr.insert(0, str(current))

def button_SQRT():
    current = math.sqrt(float(display_scr.get()))
    display_scr.delete(0, END)
    display_scr.insert(0, str(current))

calc = Frame(root)


# =============================Menu and Functions==================
def iExit():
    iExit = tkinter.messagebox.askyesno("Simple Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("468x540+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")

# ===================================================
# creating widgets and showing them on the screen
display_scr = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=29, borderwidth=5, cursor="arrow ")

button_7 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="7",
                  command=lambda: button_click(7)).grid(row=2, column=0)
button_8 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="8",
                  command=lambda: button_click(8)).grid(row=2, column=1)
button_9 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="9",
                  command=lambda: button_click(9)).grid(row=2, column=2)
button_4 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="4",
                  command=lambda: button_click(4)).grid(row=3, column=0)
button_5 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="5",
                  command=lambda: button_click(5)).grid(row=3, column=1)
button_6 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="6",
                  command=lambda: button_click(6)).grid(row=3, column=2)
button_1 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="1",
                  command=lambda: button_click(1)).grid(row=4, column=0)
button_2 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="2",
                  command=lambda: button_click(2)).grid(row=4, column=1)
button_3 = Button(calc, width=6, height=2, bd=4, font=('arial', 20, 'bold'), text="3",
                  command=lambda: button_click(1)).grid(row=4, column=2)
botton_add = Button(calc, text="+", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                    command=lambda: button_click('+'))
botton_sub = Button(calc, text="-", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                    command=lambda: button_click('-'))
botton_div = Button(calc, text="÷", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                    command=lambda: button_click('/'))
botton_mult = Button(calc, text="*", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                     command=lambda: button_click('*'))
botton_dot = Button(calc, text=".", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                    command=lambda: button_click('.'))
botton_equal = Button(calc, text="=", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                      command=evaluate_expression)
botton_clearAll = Button(calc, text=chr(67), width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                         command=button_clearAll).grid(row=1, column=0, pady=1)
botton_clear = Button(calc, text=chr(67) + chr(69), width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                      command=button_clear).grid(row=1, column=1, pady=1)
botton_sqrt = Button(calc, text="√", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                     command=button_SQRT).grid(row=1, column=2, pady=1)
botton_zero = Button(calc, text="0", width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                     command=lambda: button_click(0)).grid(row=5, column=0, pady=1)
bottonPM = Button(calc, text=chr(177), width=6, height=2, bd=4, bg="#FFE933", font=('arial', 20, 'bold'),
                  command=mathPM).grid(row=5, column=2, pady=1)

calc.grid()
display_scr.grid(row=0, column=0, columnspan=4, padx=0, pady=10)
botton_mult.grid(row=3, column=3)
botton_sub.grid(row=2, column=3)
botton_add.grid(row=1, column=3)
botton_dot.grid(row=5, column=1)
botton_div.grid(row=4, column=3)
botton_equal.grid(row=5, column=3)


root.config(menu=menubar)
root.mainloop()
