from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Simple Calculator")

lbl1 = Label(window,text="Enter 1st Number: ")
lbl1.place(x=50,y=50)

lbl2 = Label(window,text="Enter 2nd Number: ")
lbl2.place(x=50,y=100)