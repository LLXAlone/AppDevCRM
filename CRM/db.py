import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = ''
)

#prepate a curor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crm_db")

print("Done creating the database.")
