import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123")

print("----------Creating Database----------")


# To create a database in MySQL, use the "CREATE DATABASE" statement:

# create a database named "MyDatabase":

"""
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MyDatabase")
"""

print("----------Check If Database Exists----------")


# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# Try connecting to the database "MyDatabase":

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")