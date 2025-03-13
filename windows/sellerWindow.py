from window import window
from tkinter import *
from tkinter import ttk
import orm

class SellerWindow:
    def __init__(self):
        self.h = orm.handler("database.db")

        self.w = window("Меню продавца", (600, 900))

        tableheading = ttk.Label(self.w.root, text="выберите товар", font=("Segoe UI bold", 16))
        tableheading.pack(expand=True, pady=20, anchor="c")

        self.productsTable = ttk.Treeview(self.w.root, columns=("id" ,"name", "price", "category"), show="headings", displaycolumns=("name", "price", "category"))
        self.productsTable.heading("id", text="ID")
        self.productsTable.heading("name", text="Название")
        self.productsTable.heading("price", text="Цена")
        self.productsTable.heading("category", text="Категория")
        self.productsTable.pack(pady= 20, anchor="n")
        self.updateTableData()
        self.productsTable.bind("<<TreeviewSelect>>", self.itemSelectedForEdit)

        mainframe = ttk.Frame(self.w.root)
        mainframe.pack(expand=True, anchor="n", padx=20)

        ttk.Label(mainframe, text="Название").grid(row=0, column=0, padx=10, pady=10)
        self.nameEntry = ttk.Entry(mainframe)
        self.nameEntry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(mainframe, text="Цена").grid(row=1, column=0, padx=10, pady=10)
        self.priceEntry = ttk.Spinbox(mainframe, from_=1.0, to_=10000000)
        self.priceEntry.grid(row=1, column =1, padx=10, pady=10)

        ttk.Label(mainframe, text="категория").grid(row=2, column=0, padx=10, pady=10)
        self.categoryEntry = ttk.Entry(mainframe)
        self.categoryEntry.grid(row=2, column=1, padx=10, pady=10)

        editButton = ttk.Button(mainframe, text="Изменить", command=self.updateSelectedProduct)
        editButton.grid(row=0, column=2, rowspan=3, ipady=20)


        addFrame = ttk.Frame(self.w.root)
        addFrame.pack(expand=True, anchor="n", padx=20)

        addHeading = ttk.Label(addFrame, text="Создать новый товар", font=("Segoe UI bold", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(addFrame, text="Название").grid(row=1, column=0, padx=10, pady=10)
        self.nameAddEntry = ttk.Entry(addFrame)
        self.nameAddEntry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(addFrame, text="Цена").grid(row=2, column=0, padx=10, pady=10)
        self.priceAddEntry = ttk.Spinbox(addFrame, from_=1.0, to_=10000000)
        self.priceAddEntry.grid(row=2, column =1, padx=10, pady=10)

        ttk.Label(addFrame, text="Категория").grid(row=3, column=0, padx=10, pady=10)
        self.categoryAddEntry = ttk.Entry(addFrame)
        self.categoryAddEntry.grid(row=3, column=1, padx=10, pady=10)

        addButton = ttk.Button(addFrame, text="Добавить", command=self.addNewProduct)
        addButton.grid(row=1, column=2, rowspan=3, ipady=20)


    def updateTableData(self):
        products = self.h.selectAll()
        self.productsTable.delete(*self.productsTable.get_children())
        for product in products:
            self.productsTable.insert("", END, values=product)

    def updateSelectedProduct(self):
        for product in self.productsTable.selection():
            selectedItem = self.productsTable.item(product)

            vals = {
                'id': selectedItem["values"][0],
                'name': self.nameEntry.get(),
                'price': self.priceEntry.get(),
                'category': self.categoryEntry.get()
            }

            self.h.editWrite(vals['id'], vals['name'], vals['price'], vals['category'])

            self.productsTable.item(product, values=(int(vals['id']), vals['name'], float(vals['price']), vals['category']))

    def addNewProduct(self):
        vals = {
            'name': self.nameAddEntry.get(),
            'price': self.priceAddEntry.get(),
            'category': self.categoryAddEntry.get()
        }
        self.h.addWrite(vals['name'], vals['price'], vals['category'])
        self.updateTableData()

    def itemSelectedForEdit(self, event):
        for product in self.productsTable.selection():
            item = self.productsTable.item(product)


            self.nameEntry.delete(0, END)
            self.priceEntry.delete(0, END)
            self.categoryEntry.delete(0,END)
            self.nameEntry.insert(0, item['values'][1])
            self.priceEntry.insert(0, item['values'][2])
            self.categoryEntry.insert(0, item['values'][3])

