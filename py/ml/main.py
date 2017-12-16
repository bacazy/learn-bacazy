# -*- coding: utf-8 -*-

import tkinter as tk
from xrd.view.MainWindow import MainWindow

win = tk.Tk()
win.wm_title("XRD")
win.geometry("1200x600")
win.resizable(width=False, height=False)
app = MainWindow(master=win)
app.mainloop()
