import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")

# Creating a Table...
# To create a table in MySQL, use the "CREATE TABLE" statement.
# Make sure you define the name of the database when you create the connection.

# Create A Table named IPL 2021:

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IPL (Standing INT AUTO_INCREMENT PRIMARY KEY, Team VARCHAR(255),Matches INT, Win INT, Lose INT, Points INT)")

# Check if Table Exists
# You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# Primary Key
# When creating a table, you should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.

