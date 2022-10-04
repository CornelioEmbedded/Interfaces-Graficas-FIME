from tkinter import *
from PIL import ImageTk, Image
import serial
import threading
import time

X_LEDS_1 = 250
X_LEDS_2 = 420
Y_LEDS_1 = 250
Y_LEDS_2 = 350 

arduino = serial.Serial('com3', 9600, timeout = 1)

class ADC(Frame):
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

                if label == 'sen[1]':
                    self.value_pot1.set(value)
                if label == 'sen[2]':
                    self.value_pot2.set(value)
                if label == 'sen[3]':
                    self.value_pot3.set(value)
                if label == 'sen[4]':
                    self.value_pot4.set(value)

    def create_widgets(self):
        WIDHT = 6

        Label(self,text="Pot[1]: ").place(x=30,y=10)
        Label(self,width=WIDHT,textvariable=self.value_pot1).place(x=70,y=10)

        Label(self,text="Pot[2]: ").place(x=30,y=50)
        Label(self,width=WIDHT,textvariable=self.value_pot2).place(x=70,y=50)

        Label(self,text="Pot[3]: ").place(x=30,y=90)
        Label(self,width=WIDHT,textvariable=self.value_pot3).place(x=70,y=90)

        Label(self,text="Pot[4]: ").place(x=30,y=130)
        Label(self,width=WIDHT,textvariable=self.value_pot4).place(x=70,y=130)

class LEDS(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=420, height=270)
        self.master = master                    
        self.pack()
        
        self.hilo_bot1 = threading.Thread(target=self.getButtonValues,daemon=True)
        self.hilo_bot2 = threading.Thread(target=self.getButtonValues,daemon=True)
        self.hilo_bot3 = threading.Thread(target=self.getButtonValues,daemon=True)
        self.hilo_bot4 = threading.Thread(target=self.getButtonValues,daemon=True)

        time.sleep(1)
        
        self.value_bot1 = IntVar()
        self.value_bot2 = IntVar()
        self.value_bot3 = IntVar()
        self.value_bot4 = IntVar()

        self.isRun=True

        self.hilo_bot1.start()
        self.hilo_bot2.start()
        self.hilo_bot3.start()
        self.hilo_bot4.start()

        self.led_off_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
        self.led_on_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))

    
    def getButtonValues(self):

        POS_1_X = 20
        POS_2_X = 230
        POS_1_Y = 50
        POS_2_Y = 150
        POS_GONE_X = 1000
        POS_GONE_Y = 0

        while self.isRun:
            cad =arduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")

                label=cad[:pos]
                value=cad[pos+1:]                 

                if label == 'sen[5]':
                    self.value_bot1.set(value)
                    Label(self, image = self.led_off_1).place(x = POS_1_X, y = POS_1_Y)
                    if self.value_bot1.get() == 0:
                        Label(self, image = self.led_on_1).place(x = POS_1_X, y = POS_1_Y)
                    else:
                        Label(self, image = self.led_on_1).place(x = POS_GONE_X, y = POS_GONE_Y)
                if label == 'sen[6]':
                    self.value_bot2.set(value)
                    Label(self, image = self.led_off_1).place(x =POS_2_X, y = POS_1_Y)
                    if self.value_bot2.get() == 0:
                        Label(self, image = self.led_on_1).place(x = POS_2_X, y = POS_1_Y)
                    else:
                        Label(self, image = self.led_on_1).place(x = POS_GONE_X, y = POS_GONE_Y)
                if label == 'sen[7]':
                    self.value_bot3.set(value)
                    Label(self, image = self.led_off_1).place(x = POS_1_X, y = POS_2_Y)
                    if self.value_bot3.get() == 0:
                        Label(self, image = self.led_on_1).place(x = POS_1_X, y = POS_2_Y)
                    else:
                        Label(self, image = self.led_on_1).place(x = POS_GONE_X, y = POS_GONE_Y)
                if label == 'sen[8]':
                    self.value_bot4.set(value)
                    Label(self, image = self.led_off_1).place(x = POS_2_X, y = POS_2_Y)
                    if self.value_bot4.get() == 0:
                        Label(self, image = self.led_on_1).place(x = POS_2_X, y = POS_2_Y)
                    else:
                        Label(self, image = self.led_on_1).place(x =POS_GONE_X, y = POS_GONE_Y)
                

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

def set_leds(led_off_1, led_off_2, led_off_3, led_off_4):

    label_led_off_1 = Label(image = led_off_1)
    label_led_off_2 = Label(image = led_off_2)
    label_led_off_3 = Label(image = led_off_3)
    label_led_off_4 = Label(image = led_off_4)

    return label_led_off_1, label_led_off_2, label_led_off_3, label_led_off_4


def show_leds_off(label_led_off_1, label_led_off_2, label_led_off_3, label_led_off_4):
    label_led_off_1.place(x = 250, y = 250)
    label_led_off_2.place(x = 420, y = 250)
    label_led_off_3.place(x = 250, y = 350)
    label_led_off_4.place(x = 420, y = 350)


