import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="athved@123",
  database="MyDatabase")


print("----------------Limit the Result----------------")

# You can limit the number of records returned from the query, by using the "LIMIT" statement:

# Select the 5 first records in the "customers" table:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM IPL LIMIT 4")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


print("----------------Start From Another Position----------------")


# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

# Start from position 3, and return 5 records:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM IPL LIMIT 8 OFFSET 4")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)