import matplotlib
matplotlib.use("TkAgg")
import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import threading 

class GUI:
    def __init__(self,  window):
        self.window = window
        self.gesture = StringVar()
        self.gesture_label = Label(window, textvariable=self.gesture)
        self.gesture_label.config(font=("Courier", 44))
        self.gesture_label.pack()
        #self.button.pack()
        #update.pack()
        self.line0, self.line1, self.line2 = None, None, None
        self.widget = None
        self.canvas = None

    def plot (self, tofs):
        if self.widget:
            self.widget.destroy()
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
        self.fig = Figure(figsize=(6,6))
        self.ax = self.fig.add_subplot(111)
        self.line0, = self.ax.plot(tofs[0], label="Channel0")
        self.line1, = self.ax.plot(tofs[1], label="Channel0")
        self.line2, = self.ax.plot(tofs[2], label="Channel0")

        self.ax.set_title ("Gesture", fontsize=16)
        self.ax.set_ylabel("Distance", fontsize=14)
        self.ax.set_xlabel("Time (ms)", fontsize=14)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack()
        self.canvas.draw()

    def update (self, tofs, gesture):
        self.gesture.set(gesture)
        if self.line0:
            self.line0.set_data(np.linspace(0, tofs.shape[1], num=tofs.shape[1]), tofs[0])
            self.line1.set_data(np.linspace(0, tofs.shape[1], num=tofs.shape[1]), tofs[1])
            self.line2.set_data(np.linspace(0, tofs.shape[1], num=tofs.shape[1]), tofs[2])
            self.ax.set_xlim(0, tofs.shape[1])
            self.ax.set_ylim(0, max(max(tofs[0]), max(tofs[1]), max(tofs[2])))
        else:
            self.plot(tofs)
            print("plotted")
        self.canvas.draw()
if __name__ == "__main__":    
    window= Tk()
    start= GUI (window)
    window.mainloop()