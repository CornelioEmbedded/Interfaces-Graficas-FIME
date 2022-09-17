from tkinter import *
from PIL import ImageTk, Image

HEIGHT = 600
WIDTH = 1200
COLOR_BACKGROUND = '#80c1ff'



root = Tk()
root.title('Interfaz Grafica')

canvas = Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

def show_leds():

    led_off_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
    led_off_2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
    led_off_3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
    led_off_4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))

    led_on_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
    led_on_2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
    led_on_3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
    led_on_4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))

    label_led_off_1 = Label(image = led_off_1)
    label_led_off_2 = Label(image = led_off_2)
    label_led_off_3 = Label(image = led_off_3)
    label_led_off_4 = Label(image = led_off_4)

    label_led_on_1 = Label(image = led_on_1)
    label_led_on_2 = Label(image = led_on_2)
    label_led_on_3 = Label(image = led_on_3)
    label_led_on_4 = Label(image = led_on_4)


    label_led_off_1.place(x =100, y = 100)
    label_led_off_2.place(x = 100, y = 200)
    label_led_off_3.place(x = 100, y = 300)
    label_led_off_4.place(x = 100, y = 400)

    label_led_on_1.place(x =300, y = 100)
    label_led_on_2.place(x = 300, y = 200)
    label_led_on_3.place(x = 300, y = 300)
    label_led_on_4.place(x = 300, y = 400)




show_leds()

# label_led_off_3.place(width=300, height=600, x=500, y=40)
# label_led_off_4.place(width=300, height=600, x=500, y=60)


root.mainloop()


