from tkinter import Frame,Label,Button,Checkbutton,Scale,StringVar,IntVar
import serial
import time
import threading


class MainFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=420, height=270)                
        self.master = master    
        self.master.protocol('WM_DELETE_WINDOW',self.askQuit)
        self.pack()
        self.hilo1 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.arduino = serial.Serial("COM3",9600,timeout=1.0)
        time.sleep(1)
        self.value_pot = StringVar()
        self.value_dis = StringVar()
        self.value_mot = StringVar()
        self.value_led = IntVar()
        self.create_widgets()
        self.isRun=True
        self.hilo1.start()

    def askQuit(self):
        self.isRun=False
        self.arduino.write('mot:0'.encode('ascii'))
        time.sleep(1.1)
        self.arduino.write('led:0'.encode('ascii'))
        self.arduino.close()
        self.hilo1.join(0.1)
        self.master.quit()
        self.master.destroy()
        print("*** finalizando...")

    def getSensorValues(self):
        while self.isRun:
            cad =self.arduino.readline().decode('ascii').strip()
            if cad:         
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == 'dis':
                    self.value_dis.set(value)                   
                if label == 'pot':
                    self.value_pot.set(value)
        

        
    def fEnviaLed(self):
        cad='led:' + str(self.value_led.get())
        self.arduino.write(cad.encode('ascii'))
        print(cad)

    def fEnviaMot(self):
        cad = "mot:" + self.value_mot.get()
        self.arduino.write(cad.encode('ascii'))
        print(cad)
        
    def create_widgets(self):
        Label(self,text="Potenciometro: ").place(x=30,y=20)
        Label(self,width=6,textvariable=self.value_pot).place(x=120,y=20)
        Label(self,text="Distancia: ").place(x=30,y=50)
        Label(self,width=6,textvariable=self.value_dis).place(x=120,y=50)
        Checkbutton(self, text="Encender/Apagar Led", variable=self.value_led,
        onvalue=1, offvalue=0,command=self.fEnviaLed).place(x=30, y=90)                 
        Label(self,text="Servo: ").place(x=30,y=132)
        Scale(self, from_=0, to=180,orient='horizontal',tickinterval=20,
         length=220,variable=self.value_mot).place(x=90,y=115)        
        Button(self,text="Enviar", command=self.fEnviaMot).place(x=330,y=130)
        
        
