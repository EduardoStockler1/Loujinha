import sqlite3
import datetime

conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM inventory WHERE ID = 12")
conn.commit()

class Product:
    def __init__(self, id, name, price, description,category, quantity):
        self.id: int = id
        self.name: str = name
        self.price: float = price
        self.description: str = description
        self.category: int = category
        self.quantity: int = quantity
    
    def  RegisterProduct(self):
        product = (self.id, self.name, self.price, self.description, self.category, self.quantity)
        cursor.execute("INSERT INTO inventory(ID, name, price, description, category, quantity) VALUES (?, ?, ?, ?, ?, ?)", product)
        conn.commit()
        print(f'Produto "{self.name}" cadastrado com sucesso!')

    def ListProduct(product):
        cursor.execute("SELECT * FROM inventory")
        return cursor.fetchall()
    
product = Product(12, "Galaxy J5", 12.40, "Celular Samsung", "Eletronicos", 40)

product.CadastrarPoroduto()
result = product.ListProduct()

print(result)

