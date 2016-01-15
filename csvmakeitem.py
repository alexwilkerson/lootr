from __future__ import print_function
import sqlite3, csv

CSV_FILE = "items.csv"

conn = sqlite3.connect("lootr.db")

cursor = conn.cursor()

with open(CSV_FILE, "rb") as myFile:
    myFileReader = csv.reader(myFile)

    next(myFileReader)

    for name, description, type, quality, rarity, is_unique in myFileReader:
        cursor.execute("INSERT INTO items (name, description, type, quality, rarity, is_unique) VALUES (?, ?, ?, ?, ?, ?)", [name, description, type, quality, rarity, is_unique])

    try:
        conn.commit()
    except sqlite3.OperationalError:
        print(sqlite3.OperationalError)
        print("Error creating item in database.")
    conn.close()
    print("done!")
