# from tkinter import Tk, Entry, Button, StringVar
#
# class Calculator:
#     def __init__(self, master):
#         master.title("Calculator")
#         master.geometry('357x420+0+0')
#         master.config(bg='black')
#         master.resizable(False, False)
#
#         self.equation = StringVar()
#         self.entry_value = ''
#         Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
#
#         Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
#         Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
#         Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
#         Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
#
#         Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=125)
#         Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=90, y=125)
#         Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=180, y=125)
#         Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
#
#         Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
#         Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
#         Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
#         Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
#
#         Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=275)
#         Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=275)
#         Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=275)
#         Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
#
#         Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)
#         Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
#         Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
#         Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
#
#     # --- ✅ Define methods properly at class level ---
#     def show(self, value):
#         self.entry_value += str(value)
#         self.equation.set(self.entry_value)
#
#     def clear(self):
#         self.entry_value = ''
#         self.equation.set(self.entry_value)
#
#     def solve(self):
#         try:
#             result = eval(self.entry_value)
#             self.equation.set(result)
#         except:
#             self.equation.set("Error")
#
# # Run the app
# root = Tk()
# calculator = Calculator(root)
# root.mainloop()


from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.config(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += str(value)
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        result = str(eval(equation))
        label_result.config(text=result)
        equation = result
    except:
        label_result.config(text="Error")
        equation = ""

# Display label
label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# --- Button Layout ---

# Row 1
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#3697f5", command=clear).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=100)

# Row 2
Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(7)).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(8)).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(9)).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

# Row 3
Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(4)).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(5)).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(6)).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

# Row 4
Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(1)).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(2)).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(3)).place(x=290, y=400)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#fe9037", command=calculate).place(x=430, y=400)

# Row 5
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(0)).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)

root.mainloop()
