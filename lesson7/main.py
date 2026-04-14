import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute(
    """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
"""
)

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alisher", 30))

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())


cursor.execute("UPDATE users SET age = ? WHERE name = ?", (19, "Alisher"))

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.execute("DELETE FROM users WHERE name = ?", ("Alisher",))

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.commit()
conn.close()
