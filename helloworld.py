import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root"
        passwd="123password"

        )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE testdb")

