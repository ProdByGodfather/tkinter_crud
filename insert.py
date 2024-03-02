from main import *

name = input("enter name: ")
family = input("enter family: ")
age = int(input("enter age: "))

cur.execute("INSERT INTO users(name, family, age) VALUES(?, ?, ?)",[name,family, age])
conn.commit()