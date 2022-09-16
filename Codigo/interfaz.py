from distutils.cmd import Command
from tkinter import *
from PIL import ImageTk, Image
from funciones import *

HEIGHT = 600
WIDTH = 1200


root = Tk()
root.title('Interfaz Grafica')


canvas = Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg = '#80c1ff')
frame.place(relwidth=1, relheight=1)

frame_teclado = Frame(root, bg = '#80c1ff')
frame_teclado.place(relwidth=0.25, relheight=0.45,x=850, y=250)

keyword(frame_teclado)

root.mainloop()
