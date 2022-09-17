from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Charts')
root.geometry('400x200')

def graph():
    house_prices_1 = np.random.normal(200000, 25000, 5000)
    house_prices_2 = np.random.normal(200000, 25000, 5000)
    house_prices_3= np.random.normal(200000, 25000, 5000)
    house_prices_4 = np.random.normal(200000, 25000, 5000)

    plt.hist(house_prices_1, 50)
    plt.hist(house_prices_2, 50)
    plt.hist(house_prices_3, 50)
    plt.hist(house_prices_4, 50)

    plt.show()

my_button = Button(root, text= 'Graphic', command= graph)
my_button.pack()

root.mainloop()