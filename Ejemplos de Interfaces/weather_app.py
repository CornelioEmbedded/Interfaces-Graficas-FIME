from tkinter import *
import tkinter

root = Tk()

canvas = Canvas(root, height= 500, width=500)

button = Button(root, text = 'Test ')

frame = Frame(root, bg = '#80c1ff')


frame.place(relwidth=1, relheight=1)
canvas.pack()
button.pack()
root = mainloop()