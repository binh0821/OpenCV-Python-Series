import mysql.connector

mydb= mysql.connector.connect(host="localhost",user="user",password="password",port="3310")

ex1="Create database `images`;"

mycursor=mydb.cursor()
mycursor.execute(ex1)