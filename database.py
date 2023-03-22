import os
import sqlite3

filename = "database.sqlite3"
data_path = "./"

if os.path.isfile(filename):
    # If the database file exists, connect to it using sqlite3
    conn = sqlite3.connect(filename)
    print("Connected to database.")
    conn.close()
else:
    os.makedirs(data_path, exist_ok=True)

    db = sqlite3.connect(data_path + filename)
    db.execute('CREATE TABLE IF NOT EXISTS Recipies (id INTEGER PRIMARY KEY, result TEXT, element1 TEXT, element2 TEXT)')
    db.close()

    print("Database Created")