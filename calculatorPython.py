#Reference: https://youtu.be/9WPmxH4RRZ0 by DJ Oamen

#Title: calculatorPython
#Author: Omar El-Shaarawi
#Date: 28/12/2020
#Describtion: Simple interactable calculator to learn Python.

from tkinter import*

def btnClick (num):
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

calc = Tk()
calc.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(calc, font = ('arial', 20, 'bold'), fg = "white", textvariable = text_Input, bd = 30, insertwidth = 4,
                     bg = "black", justify = 'right').grid(columnspan = 4)

#===================================================================================

btn7 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "7", bg = "black", command = lambda:btnClick(7)).grid(row = 1, column = 0)
                
btn8 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "8", bg = "black", command = lambda:btnClick(8)).grid(row = 1, column = 1)

btn9 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "9", bg = "black", command = lambda:btnClick(9)).grid(row = 1, column = 2)

btnPlus = Button(calc, padx = 22, bd = 8, fg = "red", font = ('arial', 20, 'bold'),
                text = "+", bg = "black", command = lambda:btnClick("+")).grid(row = 1, column = 3)

#===================================================================================

btn4 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "4", bg = "black", command = lambda:btnClick(4)).grid(row = 2, column = 0)

btn5 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "5", bg = "black", command = lambda:btnClick(5)).grid(row = 2, column = 1)
                
btn6 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "6", bg = "black", command = lambda:btnClick(6)).grid(row = 2, column = 2)

btnMinus = Button(calc, padx = 22, bd = 8, fg = "red", font = ('arial', 20, 'bold'),
                text = "-", bg = "black", command = lambda:btnClick("-")).grid(row = 2, column = 3)

#===================================================================================

btn1 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "1", bg = "black", command = lambda:btnClick(1)).grid(row = 3, column = 0)

btn2 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "2", bg = "black", command = lambda:btnClick(2)).grid(row = 3, column = 1)

btn3 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "3", bg = "black", command = lambda:btnClick(3)).grid(row = 3, column = 2)

btnMultiply = Button(calc, padx = 22, bd = 8, fg = "red", font = ('arial', 20, 'bold'),
                text = "*", bg = "black", command = lambda:btnClick("*")).grid(row = 3, column = 3)

#===================================================================================

btnClear = Button(calc, padx = 19, bd = 8, fg = "red", font = ('arial', 20, 'bold'),
                text = "C", bg = "black", command = btnClearDisplay).grid(row = 4, column = 0)

btn0 = Button(calc, padx = 19, bd = 8, fg = "white", font = ('arial', 20, 'bold'),
                text = "0", bg = "black", command = lambda:btnClick(0)).grid(row = 4, column = 1)

btnEqual = Button(calc, padx = 19, bd = 8, fg = "red", font = ('arial', 20, 'bold'),
                text = "=", bg = "black", command = btnEqualInput).grid(row = 4, column = 2)

btnDivided = Button(calc, padx = 22, bd = 8, fg = "red", font = ('arial', 20, 'bold'),
                text = "/", bg = "black", command = lambda:btnClick("/")).grid(row = 4, column = 3)

#===================================================================================

calc.mainloop()
