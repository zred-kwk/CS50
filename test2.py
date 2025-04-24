import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='sakila')

mycursor = mydb.cursor()

mycursor.execute('show tables')

result = mycursor.fetchall()

for i in result:
    print(i)

def view_table(name):
    df = pd.read_sql_query(f"SELECT * FROM {name} LIMIT 5",mydb)
    print(df)

view_table('film')