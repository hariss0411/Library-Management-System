import sys
import sqlite3
import pandas as pd
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
cat = " ".join(sys.argv[1:])
cursor.execute("select Title from books where Genre=?", (cat,))
rs = cursor.fetchall()
a=[]
for i in rs:
    a+=(i)
s=("\n".join(a))
print(s)
'''need = input("\nWhich book would you like to read : ")
cursor.execute("select Count_books from books where Title=?", (need,))
rs = cursor.fetchone()
if rs[0] == 0:
    print(a,"\nCurrently book not avaialabe !!")
else:
    print("\nBook is available in Library. Contact Librarian to issue...")'''