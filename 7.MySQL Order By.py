import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="athved@123",
  database="MyDatabase")

print("----------------Sort The Result----------------")

#Use the ORDER BY statement to sort the result in ascending or descending order.
#The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order,
# use the DESC keyword.

#Sort the result alphabetically by Team: result:

mycursor = mydb.cursor()
sql = "SELECT * FROM IPL ORDER BY Team"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


print("----------------Order By Desc----------------")


#Use the DESC keyword to sort the result in a descending order.

#Sort the result reverse alphabetically by name:


mycursor = mydb.cursor()
sql = "SELECT * FROM IPL ORDER BY Team DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
