#import sqlite3
#establish the connectie with db file
#conn=sqlite3.connect("you.db")
#create a cursor object for CROD Operationd
#cursor=conn.cursor()
#print("database connected successfully")
#conn.close()


import sqlite3

conn = sqlite3.connect("you.db")
print("Database connected successfully!")

conn.close()