from tkinter import *
from tkinter.ttk import *
import math

def place(text):
    curr_Text = entryText.get()
    if curr_Text == "Error":
        entryText.set(text)
    else:
        entryText.set(curr_Text + text)


def sq_root():
    try:
        num = equate()
        entryText.set(math.sqrt(num))
    except:
        entryText.set("Error")


def square():
    try:
        num = equate()
        entryText.set(num**2)
    except:
        pass


def equate():
    try:
        equation = entryText.get()
        entryText.set(eval(equation))
        result = int(entryText.get())
        return result
    except:
        pass


def fact():
    num = equate()

    if num == 0 or num == 1:
        entryText.set("1")
    else:
        try:
            num = int(num)
            ans = 1
            for i in range(2, num + 1):
                ans *= i
                if ans > 10**9:
                    ans = "Cant handle this big. (That's what she said)"
                    break
            entryText.set(ans)
        except:
            entryText.set("Error")

def clear():
    entryText.set("")


root = Tk()
root.title("Calculator")
root.configure(background = "red")

global result, equation

entryText = StringVar()
equation = ""
result = 0

entry = Entry(width = 50, textvariable = entryText)
entry.grid(row = 1, column = 1, columnspan = 4, padx = 2, pady = 3)
entry.focus()

Root = Button(text = "√", command = lambda: sq_root()).grid(row = 2, column = 1)
Square = Button(text = "x²", command = lambda: square()).grid(row = 2, column = 2)
Mod = Button(text = "x!", command = lambda: fact()).grid(row = 2, column = 3)
Clear = Button(text = "C", command = lambda: clear()).grid(row = 2, column = 4)

B7 = Button(text = "7", command = lambda: place("7")).grid(row = 3, column = 1)
B8 = Button(text = "8", command = lambda: place("8")).grid(row = 3, column = 2)
B9 = Button(text = "9", command = lambda: place("9")).grid(row = 3, column = 3)
Division = Button(text = "÷", command = lambda: place("/")).grid(row = 3, column = 4)

B4 = Button(text = "4", command = lambda: place("4")).grid(row = 4, column = 1)
B5 = Button(text = "5", command = lambda: place("5")).grid(row = 4, column = 2)
B6 = Button(text = "6", command = lambda: place("6")).grid(row = 4, column = 3)
Multiply = Button(text = "x", command = lambda: place("x")).grid(row = 4, column = 4)

B1 = Button(text = "1", command = lambda: place("1")).grid(row = 5, column = 1)
B2 = Button(text = "2", command = lambda: place("2")).grid(row = 5, column = 2)
B3 = Button(text = "3", command = lambda: place("3")).grid(row = 5, column = 3)
Minus = Button(text = "-", command = lambda: place("-")).grid(row = 5, column = 4)

B0 = Button(text = "0", command = lambda: place("0")).grid(row = 6, column = 1)
Decimal = Button(text = ".", command = lambda: place(".")).grid(row = 6, column = 2)
Equal = Button(text = "=", command = lambda: equate()).grid(row = 6, column = 3)
Plus = Button(text = "+", command = lambda: place("+")).grid(row = 6, column = 4)

root.mainloop()
