from tkinter import *
from math import sqrt



# ---------- FUNCTION DEFINITIONS ----------

# function to execute when button is clicked
def buttonClick(symbol):
    currentValues = e.get()
    e.delete(0, END)
    e.insert(0, str(currentValues) + str(symbol))


def buttonClearBox():
    e.delete(0, END)


def buttonClearAll():
    e.delete(0, END)
    global savedValue
    savedValue = 0


def buttonCopy():
    global savedValue
    savedValue = int(e.get())
    e.delete(0, END)


def buttonPaste():
    e.delete(0, END)
    e.insert(0, str(savedValue))


def buttonOperation(op_type):
    global partialResult
    partialResult = int(e.get())
    e.delete(0, END)
    global flagOP
    flagOP = op_type


def buttonResult():
    result = e.get()
    e.delete(0, END)
    if flagOP == "add":
        e.insert(0, str(int(result) + int(partialResult)))
    elif flagOP == "sub":
        e.insert(0, str(int(partialResult) - int(result)))
    elif flagOP == "mult":
        e.insert(0, str(int(result) * int(partialResult)))
    elif flagOP == "div":
        e.insert(0, str(int(int(partialResult) / int(result))))
    else:
        print("ERROR 100")


def buttonSQRT():
    number = int(e.get())
    sqrtNumber = int(sqrt(number))
    e.delete(0, END)
    e.insert(0, str(sqrtNumber))







# ---------- VARIABLE DEFINITIONS ----------

root = Tk()
root.title("Simple Calculator (Integers Only)")
e = Entry(root, width=75, borderwidth=4)

# defining button for the digits from 0 to 9
buttons_x_size = 16
buttons_y_size = 16
button_1 = Button(root, text="1", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(1))
button_2 = Button(root, text="2", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(2))
button_3 = Button(root, text="3", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(3))
button_4 = Button(root, text="4", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(4))
button_5 = Button(root, text="5", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(5))
button_6 = Button(root, text="6", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(6))
button_7 = Button(root, text="7", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(7))
button_8 = Button(root, text="8", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(8))
button_9 = Button(root, text="9", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(9))
button_0 = Button(root, text="0", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonClick(0))
# defining button for the digits from 0 to 9



# defining operations buttons
button_plus = Button(root, text="+", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonOperation("add"))
button_minus = Button(root, text="-", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonOperation("sub"))
button_mult = Button(root, text="*", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonOperation("mult"))
button_div = Button(root, text="/", width=buttons_x_size, pady=buttons_y_size, command=lambda: buttonOperation("div"))
button_sqrt = Button(root, text="sqrt", width=buttons_x_size, pady=buttons_y_size, command=buttonSQRT)
button_result = Button(root, text="=", width=buttons_x_size, pady=buttons_y_size, command=buttonResult)
# defining operations buttons

# functionality buttons
button_clear_box = Button(root, text="C", width=buttons_x_size, pady=buttons_y_size, command=buttonClearBox)
button_clear_all = Button(root, text="CLR", width=buttons_x_size, pady=buttons_y_size, command=buttonClearAll)
button_copy_value = Button(root, text="Copy", width=buttons_x_size, pady=buttons_y_size, command=buttonCopy)
button_paste_value = Button(root, text="Paste", width=buttons_x_size, pady=buttons_y_size, command=buttonPaste)
# functionality buttons






# ---------- SCREEN OPERATIONS ----------

# input text bar
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)

button_plus.grid(row=5, column=2)
button_minus.grid(row=5, column=0)
button_mult.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_sqrt.grid(row=4, column=3)

button_result.grid(row=5, column=3)

button_clear_box.grid(row=1, column=0)
button_clear_all.grid(row=1, column=1)
button_copy_value.grid(row=1, column=2)
button_paste_value.grid(row=1, column=3)


root.mainloop()