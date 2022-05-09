# Reference: https://youtu.be/9WPmxH4RRZ0 by DJ Oamen

# Title: calculatorPython
# Author: Omar El-Shaarawi
# Date: 28/12/2020
# Describtion: Simple interactable calculator to learn Python.

from tkinter import *


def btnClick(num):
    global operator
    operator = operator + str(num)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


def btnValue(value, row, column, pad, color):
    Button(calc, padx=pad, bd=8, fg=color, font=('arial', 20, 'bold'),
           text=value, bg="black", command=lambda: btnClick(value)).grid(row=row, column=column)


calc = Tk()
calc.title("Calculator")
operator = ""
text_Input = StringVar()

# txtDisplay
Entry(calc, font=('arial', 20, 'bold'), fg="white", textvariable=text_Input, bd=30, insertwidth=4,
      bg="black", justify='right').grid(columnspan=4)

# ===================================================================================
#btn7
btnValue(7, 1, 0, 19, "white")

#btn8
btnValue(8, 1, 1, 19, "white")

#btn9
btnValue(9, 1, 2, 19, "white")

#btnPlus
btnValue("+", 1, 3, 22, "red")

# ===================================================================================

# btn4
btnValue(4, 2, 0, 19, "white")

# btn5
btnValue(5, 2, 1, 19, "white")

# btn6
btnValue(6, 2, 2, 19, "white")

# btnMinus
btnValue("-", 2, 3, 22, "red")

# ===================================================================================

# btn1
btnValue(1, 3, 0, 19, "white")

# btn2
btnValue(2, 3, 1, 19, "white")

# btn3
btnValue(3, 3, 2, 19, "white")

# btnMultiply
btnValue("*", 3, 3, 22, "red")

# ===================================================================================

# btnClear
Button(calc, padx=19, bd=8, fg="red", font=('arial', 20, 'bold'),
       text="C", bg="black", command=btnClearDisplay).grid(row=4, column=0)

btnValue(0, 4, 1, 19, "white")

Button(calc, padx=19, bd=8, fg="red", font=('arial', 20, 'bold'),
       text="=", bg="black", command=btnEqualInput).grid(row=4, column=2)

btnValue("/", 4, 3, 22, "red")

# ===================================================================================

calc.mainloop()
