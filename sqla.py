# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

#create a new database if the database doesn't already exist
conn = sqlite3.connect("lootr.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE items
               (id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, description TEXT NOT NULL, type TEXT NOT NULL, quality
               INT NOT
               NULL, rarity INT NOT NULL, is_unique INT)
               """)

# close the database connection
conn.close()
