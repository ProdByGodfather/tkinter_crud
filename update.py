from main import cur, conn

# cur.execute("UPDATE users SET age = 20 WHERE name='dr'")


cur.execute("UPDATE users SET name = 'godfather' WHERE name = 'dr'")
conn.commit()