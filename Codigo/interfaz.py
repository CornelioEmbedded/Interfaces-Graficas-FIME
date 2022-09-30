from distutils.cmd import Command
from tkinter import *
from PIL import *
from funciones import *
import serial, time

HEIGHT = 600
WIDTH = 1200
COLOR_BACKGROUND = '#80c1ff'
COLOR_SHAPE = 	"#FF4040"

root = Tk()
root.title('Interfaz Grafica')

led_off_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
led_off_2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
led_off_3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
led_off_4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
led_on_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
led_on_2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
led_on_3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
led_on_4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))

canvas = Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

frame_background = Frame(root, bg = COLOR_BACKGROUND)
frame_background.place(width=WIDTH, height=HEIGHT)

frame_keyword_zone = Frame(root, bg = COLOR_BACKGROUND, bd = 5)
frame_keyword_zone.place(width=300, height=600, x=1000, y=0, anchor = N)

frame_leds_zone = Frame(root, bg = COLOR_BACKGROUND, bd = 5)
frame_leds_zone.place(width=300, height=600, x = 600, y = 0, anchor = N)

frame_pot = Frame(root, bg = COLOR_BACKGROUND, bd = 5)
frame_pot.place(width=300, height=600, x = 200, y = 0, anchor = N)

frame_keyword = Frame(root, bg = COLOR_SHAPE, bd = 5)
frame_keyword.place(width=297, height=265, x=1000, y=250, anchor = N)

ADC_background(frame_pot)

keyword(frame_keyword)

off_1, off_2, off_3, off_4, on_1, on_2, on_3, on_4 = set_leds(led_off_1, led_off_2, led_off_3, led_off_4, led_on_1, led_on_2, led_on_3,led_on_4)

show_leds_off(off_1, off_2, off_3, off_4)

decision = 0

ADC(frame_pot)

while decision == 0:

    num = int(input('Digite un numero: '))
    single_led(num, on_1, on_2, on_3, on_4)

        


root.mainloop()
