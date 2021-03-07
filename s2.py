import sys
import sqlite3
import pandas as pd
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
need = " ".join(sys.argv[1:])
cursor.execute("select Count_books from books where Title=?", (need,))
rs = cursor.fetchone()
if not rs[0]:
    print(a,"\nCurrently book not avaialabe !!")
else:
    print("\nBook is available in Library. Contact Librarian to issue...")