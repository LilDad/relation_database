import psycopg2
from config import DATABASE

conn = psycopg2.connect(**DATABASE)

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM customers WHERE customerid=1;")
    print(cursor.fetchall())