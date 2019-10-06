import psycopg2
from config import DATABASE

conn = psycopg2.connect(**DATABASE)

with conn.cursor() as cursor:
    cursor.execute("""SELECT * FROM customers;""")
    # cursor.execute("INSERT INTO customers VALUES('123')")
    print(cursor.fetchall())
    # conn.commit