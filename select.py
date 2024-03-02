from main import cur, conn
import os

os.system("cls")
os.system('color 02')

age = int(input("Enter Age:"))

print("------------------ users ------------------")

users = cur.execute("SELECT * FROM users WHERE age > ?",[age])

for user in users:
    print(f"id: {user[0]} | name: {user[1]} | family: {user[2]} | age: {user[3]}")