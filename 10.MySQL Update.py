import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="athved@123",
  database="MyDatabase")


print("----------------Update Table----------------")


# You can update existing records in a table by using the "UPDATE" statement:

# Overwrite the Team column from "Chennai Super Kings" to "Super Kings":

"""
mycursor = mydb.cursor()
sql = "UPDATE IPL SET Team = 'Chennai Super Kings' WHERE Team = 'Super Kings'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
"""


print("----------------Prevent SQL Injection----------------")


# It is considered a good practice to escape the values of any query, also in update statements.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# The mysql.connector module uses the placeholder %s to escape values in the delete statement:

# Escape values by using the placholder %s method:

"""
mycursor = mydb.cursor()
sql = "UPDATE IPL SET Team = %s WHERE Team = %s"
val = ("Chennai Super Kings", "Super Kings")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
"""