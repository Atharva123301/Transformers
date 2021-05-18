import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")

print("----------------Select With A Filter----------------")

# When selecting records from a table, you can filter the selection by using the "WHERE" statement:

# Select record(s) where the Team is "Chennai Super Kings": result:

mycursor = mydb.cursor()
sql = "SELECT * FROM IPL WHERE Team ='Chennai Super Kings'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("----------------Wildcard Characters----------------")

# You can also select the records that starts, includes, or ends with a given letter or phrase.
# Use the %  to represent wildcard characters:

# Select records where the address contains the word "way":

mycursor = mydb.cursor()
sql = "SELECT * FROM IPL WHERE Team LIKE '%Kings%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


print("----------------Prevent SQL Injection----------------")


#When query values are provided by the user, you should escape the values.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module has methods to escape query values:

#Escape query values by using the placholder %s method:


mycursor = mydb.cursor()
sql = "SELECT * FROM IPL WHERE Team = %s"
adr = ("Chennai Super Kings",)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
