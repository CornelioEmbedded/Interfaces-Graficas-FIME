from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 


def plot_1(): 
  
    
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    y = [i**2 for i in range(101)] 
  
    
    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
    
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 

    canvas.get_tk_widget().pack() 
    
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 

    canvas.get_tk_widget().pack() 

def plot_2(): 
  
    
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    y = [i**2 for i in range(101)] 
  
    
    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
    
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 

    canvas.get_tk_widget().pack() 
    
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 

    canvas.get_tk_widget().pack() 

def plot_3(): 
  
    
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    y = [i**2 for i in range(101)] 
  
    
    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
    
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 

    canvas.get_tk_widget().pack() 
    
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 

    canvas.get_tk_widget().pack() 

def plot_4(): 
  
    
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    y = [i**2 for i in range(101)] 
  
    
    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
    
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 

    canvas.get_tk_widget().pack() 
    
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 

    canvas.get_tk_widget().pack() 
  
window = Tk() 
  
window.title('Plotting in Tkinter') 
  
window.geometry("500x500") 


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


plot_4()
# plot_button = Button(master = window, command = plot, height = 2, width = 10, text = "Plot") 
  
# plot_button.pack() 
  
window.mainloop()