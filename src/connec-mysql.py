import mysql.connector

mydb= mysql.connector.connect(host="127.0.0.1",user="root",password="pass",port="3310")

ex1="Create database `images`;"

mycursor=mydb.cursor()
mycursor.execute(ex1)