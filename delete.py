from main import cur, conn

id = int(input("Enter Id To delete: "))

cur.execute("DELETE FROM users WHERE id=?",[id])
conn.commit()