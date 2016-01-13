from __future__ import print_function
import sqlite3

print("#item creator for lootr")
name = raw_input("item name: ")
description = raw_input("description: ")
type = raw_input("type: ")
quality = raw_input("quality (1-5): ")
quality = int(quality)
rarity = raw_input("rarity (1-7): ")
rarity = int(rarity)
is_unique = raw_input("is item unique? (y/n)")
if is_unique == "y":
    is_unique = 1
else:
    is_unique = 0

conn = sqlite3.connect("lootr.db")

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO items (name, description, type, quality, rarity, is_unique) VALUES (?, ?, ?, ?, ?, ?)",
                  [name, description, type, quality, rarity, is_unique])
    conn.commit()
except sqlite3.OperationalError:
    print(sqlite3.OperationalError)
    print("Error creating item in database.")

conn.close()
