import sqlite3
conn = sqlite3.connect("you.db")
cursor = conn.cursor()
cursor.execute("""
INSERT INTO you ( name, attendance, marks, result)
VALUES (?, ?, ?, ?)
""", ( "Rahul", 85, 78, "Pass"))
conn.commit()
conn.close()
print("Student record inserted")                              