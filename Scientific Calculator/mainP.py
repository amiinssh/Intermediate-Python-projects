from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
        
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)        

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)
        
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current) 
        
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current) 
        
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)     
        
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
        
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)              
        
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current) 
        
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)             

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)


added_value = Calc()

txtDisplay = Entry(
    calc, font=("arial", 20, "bold"), bg="powder blue", bd=30, width=28, justify=RIGHT
)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(
            Button(
                calc,
                width=6,
                height=2,
                font=("arial", 20, "bold"),
                bd=4,
                text=numberpad[i],
            )
        )
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

btnclear = Button(
    calc,
    text=chr(67),
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.clear_entry
)
btnclear.grid(row=1, column=0, pady=1)

btnAllclear = Button(
    calc,
    text=chr(67) + chr(69),
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.all_clear_entry
)
btnAllclear.grid(row=1, column=1, pady=1)

btnSq = Button(
    calc,
    text="√",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.squared
)
btnSq.grid(row=1, column=2, pady=1)

btnAdd = Button(
    calc,
    text="+",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=lambda: added_value.operation("add"),
)
btnAdd.grid(row=1, column=3, pady=1)

btnSub = Button(
    calc,
    text="-",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=lambda: added_value.operation("sub"),
)
btnSub.grid(row=2, column=3, pady=1)

btnMult = Button(
    calc,
    text="*",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=lambda: added_value.operation("multi"),
)
btnMult.grid(row=3, column=3, pady=1)

btnDiv = Button(
    calc,
    text=chr(247),
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=lambda: added_value.operation("divide"),
)
btnDiv.grid(row=4, column=3, pady=1)

btnZero = Button(
    calc,
    text="0",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=lambda: added_value.numberEnter(0),
)
btnZero.grid(row=5, column=0, pady=1)

btnDot = Button(
    calc,
    text=".",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=lambda: added_value.numberEnter("."),
)
btnDot.grid(row=5, column=1, pady=1)

btnPM = Button(
    calc,
    text=chr(177),
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.mathsPM
)
btnPM.grid(row=5, column=2, pady=1)

btnEqual = Button(
    calc,
    text="=",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.sum_of_total
)
btnEqual.grid(row=5, column=3, pady=1)

btnCos = Button(
    calc,
    text="cos",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.cos
)
btnCos.grid(row=2, column=4, pady=1)

btnSin = Button(
    calc,
    text="sin",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.sin
)
btnSin.grid(row=3, column=4, pady=1)

btnTan = Button(
    calc,
    text="tan",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=added_value.tan
)
btnTan.grid(row=4, column=4, pady=1)

btnExit = Button(
    calc,
    text="Exit",
    width=6,
    height=2,
    font=("arial", 20, "bold"),
    bd=4,
    bg="powder blue",
    command=root.quit
)
btnExit.grid(row=6, column=3, pady=1)

root.mainloop()
