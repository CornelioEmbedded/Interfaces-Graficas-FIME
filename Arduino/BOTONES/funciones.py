from tkinter import Frame,Label,Button,Checkbutton,Scale,StringVar,IntVar
import serial
import time
import threading

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=420, height=270)
        self.master = master                    
        self.pack()
        
        self.hilo_pot1 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo_pot2 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo_pot3 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.hilo_pot4 = threading.Thread(target=self.getSensorValues,daemon=True)

        self.arduino = serial.Serial("COM3",9600)
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
            cad =self.arduino.readline().decode('ascii').strip()
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