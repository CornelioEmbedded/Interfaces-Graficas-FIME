from distutils.cmd import Command
from tkinter import *
from PIL import ImageTk, Image
from funciones import *

HEIGHT = 600
WIDTH = 1200
COLOR_BACKGROUND = '#80c1ff'

root = Tk()
root.title('Interfaz Grafica')


canvas = Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

# frame = Frame(root, bg = '#80c1ff')
# frame.place(relwidth=1, relheight=1)

frame_background = Frame(root, bg = COLOR_BACKGROUND)
frame_background.place(width=WIDTH, height=HEIGHT)

frame_keyword_zone = Frame(root, bg = COLOR_BACKGROUND, bd = 5)
frame_keyword_zone.place(width=300, height=600, x=1000, y=0, anchor = N)

frame_leds = Frame(root, bg = COLOR_BACKGROUND, bd = 5)
frame_leds.place(width=300, height=600, x = 600, y = 0, anchor = N)

frame_pot = Frame(root, bg = COLOR_BACKGROUND, bd = 5)
frame_pot.place(width=300, height=600, x = 200, y = 0, anchor = N)

frame_keyword = Frame(root, bg = '#00C957', bd = 5)
frame_keyword.place(width=297, height=265, x=1000, y=250, anchor = N)

keyword(frame_keyword)

root.mainloop()
