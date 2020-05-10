# Copyright 2020 by Chua Teck Lee.
# All rights reserved.

#USING SQLITE3 DATABASE TO STORE and READ info
#USING DB FOR SQLITE DATABASE TO EDIT/READ


import sqlite3
from sqlite3 import Error

class Input():
    def __init__(self, name, filepath, display, fileDisplay, buttonLayout, character):
        self.name = name
        self.filepath = filepath
        self.display = display
        self.fileDisplay = fileDisplay
        self.buttonLayout = buttonLayout
        self.character = character

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

#data
Inputs = []

conn = create_connection(r"C:\Dev\Python\Projects\Tekinput\TekinputGenerator\database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM Inputs")

rows = cur.fetchall()

for row in rows:
    Inputs.append( Input(row[0], row[1], row[2], row[3], tuple(eval(row[4])), row[5] ))



characters = []

cur.execute("SELECT * FROM Characters")

rows = cur.fetchall()

for row in rows:
    characters.append(row[0])
#     characters.append( Input(row[0], row[1], row[2], row[3], tuple(eval(row[4])) ))