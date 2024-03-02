import sqlite3

# create or connect to Database
conn = sqlite3.connect("dr.db")
# cursor conn
cur = conn.cursor()

try:
    # Make Table
    cur.execute("CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT, name varchar(255), family varchar(255), age int)")
except:
    pass

