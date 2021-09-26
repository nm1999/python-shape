import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user ="root",
    password ="",
    database ="student",
)
cursor = con.cursor()
query = cursor.execute("select * from comments")
row =cursor.fetchall()
print(row)