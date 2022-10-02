import serial
from tkinter import *

display1 = serial.Serial('com3', 9600, timeout = 1)

def display_1():
    display1.write(b'1')

def display_0():
    display1.write(b'0')

root = Tk()

button_1 = Button(root, text='1', command = display_1)
button_1.grid(row = 0, column=0)

button_0 = Button(root, text='0', command = display_0)
button_0.grid(row = 1, column=1)

root.mainloop()