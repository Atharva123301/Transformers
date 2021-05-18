#Python can be used in database applications
#One of the most popular databases is MySQL.....

#Start by creating a connection to the database.
#Use the username and password from your MySQL database:

print("----------Create Connection----------")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="athved@123")

print(mydb)