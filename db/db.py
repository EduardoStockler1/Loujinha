import sqlite3

conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

Batata = [
    (20, "Batata", 100, 1.50, "Fornecedor A"),
]

#for item in Batata:
#    cursor.execute("INSERT INTO estoque (id, descricao, quantidade, preco, fornecedor) VALUES (?, ?, ?, ?, ?)", item)

cursor.execute("SELECT * FROM estoque")

Result = cursor.fetchall()

for linha in Result:
    print(linha)

conn.commit()

conn.close()