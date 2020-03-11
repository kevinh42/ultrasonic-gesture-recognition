import matplotlib
matplotlib.use("TkAgg")
import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        update = Button (window, text="update", command=self.update)
        self.box.pack ()
        self.button.pack()
        update.pack()
        self.line = None
        self.widget = None
        self.canvas = None

    def plot (self):
        if self.widget:
            self.widget.destroy()
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
        self.fig = Figure(figsize=(6,6))
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot(x, v,color='blue')
        self.ax.invert_yaxis()

        self.ax.set_title ("Estimation Grid", fontsize=16)
        self.ax.set_ylabel("Y", fontsize=14)
        self.ax.set_xlabel("X", fontsize=14)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack()
        self.canvas.draw()

    def update (self):
        if self.line:
            x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,0])
            self.line.set_data(x, v)
            self.canvas.draw()

window= Tk()
start= mclass (window)
window.mainloop()