from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Simple Calculator")

lbl1 = Label(window,text="Enter 1st Number: ")
lbl1.place(x=50,y=50)

lbl2 = Label(window,text="Enter 2nd Number: ")
lbl2.place(x=50,y=100)

lbl3 = Label(window,text="Result: ")
lbl3.place(x=80,y=150)

t1 = Entry()
t1.place(x=180,y=50)

t2 = Entry()
t2.place(x=180,y=100)

t3 = Entry()
t3.place(x=180,y=150)

b1 = Button(window, text="Add",command=add)
b1.place(x=50,y=200)

def add():
  num1=int(t1.get())
  num2=int(t2.get())
  sum = num1 + num2
  t3.insert(END,str(sum))