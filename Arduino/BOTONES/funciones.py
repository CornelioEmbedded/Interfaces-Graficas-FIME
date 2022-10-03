from tkinter import Frame,Label,Button,Checkbutton,Scale,StringVar,IntVar
import serial
import time
import threading
from PIL import ImageTk, Image

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=420, height=270)
        self.master = master                    
        self.pack()
        
        self.hilo_bot1 = threading.Thread(target=self.getButtonValues,daemon=True)
        self.hilo_bot2 = threading.Thread(target=self.getButtonValues,daemon=True)
        self.hilo_bot3 = threading.Thread(target=self.getButtonValues,daemon=True)
        self.hilo_bot4 = threading.Thread(target=self.getButtonValues,daemon=True)

        self.arduino = serial.Serial("COM3",9600)
        time.sleep(1)
        
        self.value_bot1 = IntVar()
        self.value_bot2 = IntVar()
        self.value_bot3 = IntVar()
        self.value_bot4 = IntVar()

        self.create_widgets()
        self.isRun=True

        self.hilo_bot1.start()
        self.hilo_bot2.start()
        self.hilo_bot3.start()
        self.hilo_bot4.start()

        self.led_off_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
        self.led_off_2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
        self.led_off_3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
        self.led_off_4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_apagado.png"))
        self.led_on_1 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
        self.led_on_2 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
        self.led_on_3 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))
        self.led_on_4 = ImageTk.PhotoImage(Image.open(r"Codigo\Imagenes\led_encendido.png"))

    
    def getButtonValues(self):
        while self.isRun:
            cad =self.arduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")

                label=cad[:pos]
                value=cad[pos+1:]                 

                if label == 'bot[1]':
                    self.value_bot1.set(value)
                    Label(self, image = self.led_off_1).place(x =0, y = 0)
                    if self.value_bot1.get() == 0:
                        Label(self, image = self.led_on_1).place(x =0, y = 0)
                    else:
                        Label(self, image = self.led_on_1).place(x =1000, y = 0)
                if label == 'bot[2]':
                    self.value_bot2.set(value)
                if label == 'bot[3]':
                    self.value_bot3.set(value)
                if label == 'bot[4]':
                    self.value_bot4.set(value)
                
    
    def create_widgets(self):
        pass