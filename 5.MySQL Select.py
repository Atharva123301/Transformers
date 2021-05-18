import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")


print("----------------Select From A Table----------------")



# To select from a table in MySQL, use the "SELECT" statement:

# Select all records from the "customers" table, and display the result:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM IPL")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Note: We use the fetchall() method, which fetches all rows from the
# last executed statement.


print("----------------Selecting Columns----------------")


# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

#Select only the Standings and Teams colums:

mycursor = mydb.cursor()
mycursor.execute("SELECT Standing,Team FROM IPL")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


print("----------------Using The Fetchone() Method----------------")


#If you are only interested in one row, you can use the fetchone() method.
#The fetchone() method will return the first row of the result:

#Fetch Only One row:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM IPL")
myresult = mycursor.fetchone()
print(myresult)