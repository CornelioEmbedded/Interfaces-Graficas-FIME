from tkinter import *

root = Tk()
root.title('Interfaz Grafica')

led = PhotoImage(file = r"Codigo\Imagenes\led_encendido.png")
led = Label(root, image = led)
led.place(x=0, y=0)

root.mainloop()