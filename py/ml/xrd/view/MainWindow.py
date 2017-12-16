# -*- coding: utf-8 -*-
import tkinter as tk

from xrd.view.FigureCanvasView import FigureCanvasView
from xrd.view.ItemListView import ItemListView


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.itemListView = ItemListView(self)
        self.pack(side=tk.LEFT,expand=True)

        self.figureView = FigureCanvasView(master=master)
        self.figureView.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
