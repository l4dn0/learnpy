from tkinter.messagebox import showinfo, askokcancel

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
        mainframe.pack(expand=True, anchor="n")

        self.productsTable = ttk.Treeview(mainframe, columns=("name", "price", "category"), show="headings")
        self.productsTable.heading("name", text="Название")
        self.productsTable.heading("price", text="Цена")
        self.productsTable.heading("category", text="Категория")
        self.productsTable.pack()
        self.updateTableData()

        buyBtn = ttk.Button(mainframe, text="купить", command=self.buySelectedProducts)
        buyBtn.pack(ipadx=5, ipady=5)


    def buySelectedProducts(self):
        pricecount = 0
        for product in self.productsTable.selection():
            item = self.productsTable.item(product)
            pricecount += float(item['values'][1])
        result = askokcancel(title="Подтверждение", message=f"Вы уверены, что хотите оплатить заказ на сумму {pricecount}?")
        showinfo("уведомление", "Оплата прошла успешно.") if result else showinfo("уведомление", "Оплата отменена.")

    def updateTableData(self):
        products = self.h.selectAll()

        for product in products:
            woid = product[1:]
            self.productsTable.insert("", END, values=woid)