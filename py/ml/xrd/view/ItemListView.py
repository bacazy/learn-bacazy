# -*- coding: utf-8 -*-
import tkinter as tk


class ItemListView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.config(width=300, height=600, bg='red')
        self.pack()
        self.propagate(0)
        self.itemlist = tk.Listbox(self)
        self.itemlist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
