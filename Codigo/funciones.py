from tkinter import *
from turtle import width
from PIL import ImageTk, Image

def click(number):
    
    print(number)

def clear():

    print('')

def keyword(frame):

    button_1 = Button(frame, text='1', padx = 40, pady= 20, command = lambda : click(1))
    button_2 = Button(frame, text='2', padx = 40, pady= 20, command = lambda : click(2))
    button_3 = Button(frame, text='3', padx = 40, pady= 20, command = lambda : click(3))
    button_4 = Button(frame, text='4', padx = 40, pady= 20, command = lambda : click(4))
    button_5 = Button(frame, text='5', padx = 40, pady= 20, command = lambda : click(5))
    button_6 = Button(frame, text='6', padx = 40, pady= 20, command = lambda : click(6))
    button_7 = Button(frame, text='7', padx = 40, pady= 20, command = lambda : click(7))
    button_8 = Button(frame, text='8', padx = 40, pady= 20, command = lambda : click(8))
    button_9 = Button(frame, text='9', padx = 40, pady= 20, command = lambda : click(9))
    button_0 = Button(frame, text='0', padx = 40, pady= 20, command = lambda : click(0))
    button_cl = Button(frame, text='Clear', padx = 79, pady= 20, command = lambda : clear())

    button_1.grid(row = 3, column = 1)
    button_2.grid(row = 3, column = 2)
    button_3.grid(row = 3, column = 3)
    button_4.grid(row = 2, column = 1)
    button_5.grid(row = 2, column = 2)
    button_6.grid(row = 2, column = 3)
    button_7.grid(row = 1, column = 1)
    button_8.grid(row = 1, column = 2)
    button_9.grid(row = 1, column = 3)
    button_0.grid(row = 4, column = 1)
    button_cl.grid(row = 4, column= 2, columnspan=2)

def set_leds(led_off_1, led_off_2, led_off_3, led_off_4, led_on_1, led_on_2, led_on_3,led_on_4):

    label_led_off_1 = Label(image = led_off_1)
    label_led_off_2 = Label(image = led_off_2)
    label_led_off_3 = Label(image = led_off_3)
    label_led_off_4 = Label(image = led_off_4)

    label_led_on_1 = Label(image = led_on_1)
    label_led_on_2 = Label(image = led_on_2)
    label_led_on_3 = Label(image = led_on_3)
    label_led_on_4 = Label(image = led_on_4)

    return label_led_off_1, label_led_off_2, label_led_off_3, label_led_off_4, label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4


def show_leds_off(label_led_off_1, label_led_off_2, label_led_off_3, label_led_off_4):
    label_led_off_1.place(x =525, y = 200)
    label_led_off_2.place(x = 525, y = 300)
    label_led_off_3.place(x = 525, y = 400)
    label_led_off_4.place(x = 525, y = 500)

def hide_leds_on(label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4):
    label_led_on_1.place(x =2000, y = 100)
    label_led_on_2.place(x = 2000, y = 200)
    label_led_on_3.place(x = 2000, y = 300)
    label_led_on_4.place(x = 2000, y = 400)

def single_led(selection, label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4):


    if selection == 1:
        label_led_on_1.place(x =525, y = 200)
    elif selection == 2:
        label_led_on_2.place(x = 525, y = 300)
    elif selection == 3:
        label_led_on_3.place(x = 525, y = 400)
    elif selection == 4:
        label_led_on_4.place(x = 525, y = 500)
    else:
        hide_leds_on(label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4)
    