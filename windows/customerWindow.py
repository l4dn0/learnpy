import orm
from window import window
from tkinter import *
from tkinter import ttk

class CustomerWindow:
    def __init__(self):
        self.h = orm.handler("database.db")

        self.w = window("Меню покупателя", (600, 400))

        tableheading = ttk.Label(self.w.root, text="выберите товар", font=("Segoe UI bold", 16))
        tableheading.pack(expand=True)

        mainframe = ttk.Frame(self.w.root)
        mainframe.pack(expand=True)

        self.productsTable = ttk.Treeview(mainframe, columns=("name", "price", "category"), show="headings")
        self.productsTable.heading("name", text="Название")
        self.productsTable.heading("price", text="Цена")
        self.productsTable.heading("category", text="Категория")
        self.productsTable.pack()

        self.updateTableData()

    def updateTableData(self):
        products = self.h.selectAll()

        for product in products:
            woid = product[1:]
            self.productsTable.insert("", END, values=woid)