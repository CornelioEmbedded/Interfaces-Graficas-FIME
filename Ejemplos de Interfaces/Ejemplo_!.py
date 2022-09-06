from tkinter import *
from turtle import color

root = Tk()

e = Entry(root, width= 50, borderwidth= 10)
e.pack()

def myClick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()


myButton = Button(root, text = 'Enter your name', command= myClick, bg = 'skyblue')

myButton.pack()

root.mainloop()