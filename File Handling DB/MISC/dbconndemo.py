#pip install psycopg2
import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
    print(conn)
except:
    print("Unable to connect to database")

