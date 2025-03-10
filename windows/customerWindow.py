from window import window
import tkinter
from tkinter import ttk

class CustomerWindow:
    def __init__(self):
        w = window("Меню покупателя", (800, 600))

        itemsTable = ttk.Treeview(w.root, columns=["id", "name", "price", "category"])
        itemsTable.pack(side="top")