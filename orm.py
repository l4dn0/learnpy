import sqlite3

class handler:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def selectAll(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def addWrite(self, name, price, category = None):
        write = (name, price, category)
        self.cursor.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)", write)
        self.connection.commit()

    def editWrite(self, id, name, price, category = None):
        write = (name, price, category, id)
        self.cursor.execute("UPDATE products SET name = ?, price = ?, category = ? WHERE id = ?", write)
        self.connection.commit()

    def deleteWrite(self, id):
        self.cursor.execute("DELETE FROM products WHERE id=?", id)
        self.connection.commit()