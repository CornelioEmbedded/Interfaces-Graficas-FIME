from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Charts')
root.geometry('400x400')

vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()
my_label = Label(root, text = horizontal.get()).pack()

root.mainloop()