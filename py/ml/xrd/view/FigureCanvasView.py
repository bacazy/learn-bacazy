# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from matplotlib.figure import Figure


class FigureCanvasView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.config(width=900, height=600)
        # self.propagate(0)

        self.figure = Figure(figsize=(8,6))
        a = self.figure.add_subplot(111)
        a.plot(arange(0,100,0.1), sin(arange(0,100,0.1)))
        self.canvas = FigureCanvasTkAgg(figure=self.figure, master=master)
        # self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.Y, expand=1)
        # self.toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        # self.toolbar.update()
        self.canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

