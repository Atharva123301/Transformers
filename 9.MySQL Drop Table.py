import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="athved@123",
  database="MyDatabase")


print("----------------Delete A Table----------------")


# You can delete an existing table by using the "Drop Table" statement:

# Delete the table "IPL":

"""
mycursor = mydb.cursor()
sql = "DROP TABLE IPL"
mycursor.execute(sql)
"""


print("----------------Delete Only if exists----------------")


#If the the table you want to delete is already deleted, or for any other reason does not exist,
# you can use the IF EXISTS keyword to avoid getting an error.

"""
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS IPL"
mycursor.execute(sql)
"""