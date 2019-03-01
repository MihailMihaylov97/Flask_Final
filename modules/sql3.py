import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute(
    "CREATE TABLE test (id serial PRIMARY KEY, name text, username text, email text, password text)")

user = (1, "jose", "jose123", "jose@abv.bg","pass123")
insert_query = "INSERT INTO test VALUES (?, ?, ?, ?, ?)"
cur.execute(insert_query, user)

conn.commit()
conn.close()