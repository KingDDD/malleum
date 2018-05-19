#!/usr/bin/env python
from Tkinter import *

window = Tk()
window.title("Damians GUI")

l1 = Label(window, text="This is a label", font=("Arial Bold",50))
l1.place(x=10,y=10)

btn1 = Button(window, text="Click Me", bg="black", fg="green", command=clicked)
btn1.place(x=10,y=70)

def clicked():
    lb1.configure(text="You pressed the Button")

window.geometry('500x400')





window.mainloop()
