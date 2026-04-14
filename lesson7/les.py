import sqlite3

conn = sqlite3.connect("test2.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute(
    """
CREATE TABLE products ( 
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
"""
)

cursor.executemany(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    [
        ("Laptop", 109120),
        ("Phone", 15000)
    ]
)

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

cursor.execute("UPDATE products SET name = ? WHERE id = ?", ("MacBook", 1))

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

cursor.execute("DELETE FROM products WHERE id = ?", (2,))

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

conn.commit()
conn.close()
