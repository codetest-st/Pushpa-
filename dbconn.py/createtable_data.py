import sqlite3
print()
conn = sqlite3.connect("you.db")
cursor= conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS YOU(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    attendance REAL,
    marks REAL,
    result TEXT
)
""")
conn.commit()
conn.close()
print("table create successfully")
                           