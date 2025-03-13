import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk

class window:
    def __init__(self, title, framesize):
        self.root = ThemedTk(theme="breeze")
        self.root.title(title)

        width, height = framesize
        self.root.geometry(f"{width}x{height}")

    def mainloop(self):
        self.root.mainloop()