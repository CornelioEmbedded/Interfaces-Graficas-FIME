from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Icons, images and exit buttons')


my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\UJSCRQU\OneDrive-Deere&Co\OneDrive - Deere & Co\Desktop\Cursos\Interfaces-Graficas-FIME\Ejemplos de Interfaces\Imagenes\atardecer.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Exit', command= root.quit)
button_quit.pack()
root.mainloop()