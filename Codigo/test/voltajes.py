from tkinter import *
from tkinter import *
from PIL import *

root = Tk()

voltage = '200 V'
voltage1 = '12 V'
voltage2 = '15 V'
voltage3 = '0 V'

voltage_1 = Message(root, text= voltage, bd = 20, font= 'BOLD')
voltage_2 = Message(root, text= voltage1, bd = 8, font= 'BOLD')
voltage_3 = Message(root, text= voltage2, bd = 8, font= 'BOLD')
voltage_4 = Message(root, text= voltage3, bd = 8, font= 'BOLD')


voltage_1.pack()
voltage_2.pack()
voltage_3.pack()
voltage_4.pack()

root.mainloop()