from tkinter import *
from PIL import ImageTk, Image
import serial
import threading
import time

arduino = serial.Serial('com3', 9600, timeout = 1)

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=420, height=270)
        self.master = master                    
        self.pack()
        
        self.hilo_pot1 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo_pot2 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo_pot3 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo_pot4 = threading.Thread(target=self.getSensorValues,daemon=True)

        time.sleep(1)
        
        self.value_pot1 = StringVar()
        self.value_pot2 = StringVar()
        self.value_pot3 = StringVar()
        self.value_pot4 = StringVar()

        self.create_widgets()
        self.isRun=True

        self.hilo_pot1.start()
        self.hilo_pot2.start()
        self.hilo_pot3.start()
        self.hilo_pot4.start()
    
    def getSensorValues(self):
        while self.isRun:
            cad = arduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")

                label=cad[:pos]
                value=cad[pos+1:]                 

                if label == 'pot[1]':
                    self.value_pot1.set(value)
                if label == 'pot[2]':
                    self.value_pot2.set(value)
                if label == 'pot[3]':
                    self.value_pot3.set(value)
                if label == 'pot[4]':
                    self.value_pot4.set(value)

    def create_widgets(self):
        Label(self,text="Pot[1]: ").place(x=30,y=20)
        Label(self,width=6,textvariable=self.value_pot1).place(x=120,y=20)

        Label(self,text="Pot[2]: ").place(x=30,y=50)
        Label(self,width=6,textvariable=self.value_pot2).place(x=120,y=50)

        Label(self,text="Pot[3]: ").place(x=30,y=80)
        Label(self,width=6,textvariable=self.value_pot3).place(x=120,y=80)

        Label(self,text="Pot[4]: ").place(x=30,y=110)
        Label(self,width=6,textvariable=self.value_pot4).place(x=120,y=110)

def click(numero):
    if numero == 1:
        arduino.write(b'1')
    elif numero == 2:
        arduino.write(b'2')
    elif numero == 3:
        arduino.write(b'3')
    elif numero == 4:
        arduino.write(b'4')
    elif numero == 5:
        arduino.write(b'5')
    elif numero == 6:
        arduino.write(b'6')
    elif numero == 7:
        arduino.write(b'7')
    elif numero == 8:
        arduino.write(b'8')
    elif numero == 9:
        arduino.write(b'9')
    elif numero == 0:
        arduino.write(b'0')

def clear():
    arduino.write(b'clear')

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
    label_led_off_1.place(x =425, y = 300)
    label_led_off_2.place(x = 600, y = 300)
    label_led_off_3.place(x = 425, y = 400)
    label_led_off_4.place(x = 600, y = 400)

def hide_leds_on(label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4):
    label_led_on_1.place(x =2000, y = 100)
    label_led_on_2.place(x = 2000, y = 200)
    label_led_on_3.place(x = 2000, y = 300)
    label_led_on_4.place(x = 2000, y = 400)

def single_led(selection, label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4):


    if selection == 1:
        label_led_on_1.place(x =425, y = 300)
    elif selection == 2:
        label_led_on_2.place(x = 600, y = 300)
    elif selection == 3:
        label_led_on_3.place(x = 425, y = 400)
    elif selection == 4:
        label_led_on_4.place(x = 600, y = 400)
    else:
        hide_leds_on(label_led_on_1, label_led_on_2, label_led_on_3, label_led_on_4)

def ADC(frame):
    voltage = '5 V'
    voltage1 = '5 V'
    voltage2 = '5 V'
    voltage3 = '5 V'

    voltage_1 = Message(frame, text= voltage, bd = 15, font= 'BOLD')
    voltage_2 = Message(frame, text= voltage1, bd = 15, font= 'BOLD')
    voltage_3 = Message(frame, text= voltage2, bd = 15, font= 'BOLD')
    voltage_4 = Message(frame, text= voltage3, bd = 15, font= 'BOLD')


    voltage_1.place(x =125, y = 250)
    voltage_2.place(x =125, y = 325)
    voltage_3.place(x =125, y = 400)
    voltage_4.place(x =125, y = 475)

def ADC_background(frame):
    X = 115
    Y = 245

    for i in range (0,4):
        frame_voltage = Frame(frame, bg= '#FF4040')
        frame_voltage.place(x =X, y = Y, width=90, height=65)

        Y += 75