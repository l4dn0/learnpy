import tkinter

class window:
    def __init__(self, title, framesize):
        self.root = tkinter.Tk()
        self.root.title(title)

        width, height = framesize
        self.root.geometry(f"{width}x{height}")

    def mainloop(self):
        self.root.mainloop()