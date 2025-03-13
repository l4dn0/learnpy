from window import window
from tkinter import ttk
from windows.customerWindow import CustomerWindow
from windows.sellerWindow import SellerWindow

class GreeterWindow:
    def __init__(self):
        self.w = window("выбор меню", [400, 200])
        label = ttk.Label(text="Выберите меню", font=("Segoe UI", 14))
        label.pack(expand=True, anchor="n", ipady=20)
        buttonsFrame = ttk.Frame()
        buttonsFrame.pack(ipady=10, expand=True, anchor="c", padx=20)
        customerButton = ttk.Button(master=buttonsFrame, text="Покупатель", command=self.openCustomerWindow)
        sellerButton = ttk.Button(master=buttonsFrame, text="продавец", command=self.openSellerWindow)
        customerButton.grid(row=0, column=0, padx=15, pady=5)
        sellerButton.grid(row=0, column=1, padx=15, pady=5)

    def openCustomerWindow(self):
        customerWindow = CustomerWindow()
        self.w.root.destroy()

    def openSellerWindow(self):
        sellerWindow = SellerWindow()
        self.w.root.destroy()

    def mainloop(self):
        self.w.mainloop()