import mysql.connector

mydb = mysql.connector.connect(
    host='yourhost',
    user='youruser',
    password='yourpassword',
    database='yourdatabase'
)

cursorSQL = mydb.cursor()
