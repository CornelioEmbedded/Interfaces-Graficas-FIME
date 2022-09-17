from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')

img1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
img2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
img3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
img4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))

image_list = [img1, img2, img3, img4]

my_label = Label(image = img1)
my_label.grid(row=0, column=0, columnspan=3)

def foward(image_number):

    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_foward = Button(root, text = '>>', command=lambda : foward(image_number + 1))
    button_back = Button(root, text = '<<', command=lambda: back(image_number - 1))

    if image_number == 4:
        button_foward = Button(root, text = '>>', state= DISABLED)

    button_back.grid(row = 1, column=0)
    button_foward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)


def back(image_number):

    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_foward = Button(root, text = '>>', command=lambda : foward(image_number + 1))
    button_back = Button(root, text = '<<', command=lambda: back(image_number - 1))

    if image_number == 0:
        button_back = Button(root, text = '<<', state= DISABLED)
    
    button_back.grid(row = 1, column=0)
    button_foward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text = '<<', command = back, state = DISABLED)
button_foward = Button(root, text = ">>", command = lambda : foward(2))

button_back.grid(row = 1, column=0)
button_foward.grid(row=1, column=2)
root.mainloop()