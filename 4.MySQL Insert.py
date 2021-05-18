import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")

# Insert Into Table
# To fill a table in MySQL, use the "INSERT INTO" statement.

# Insert a record in the "customers" table:

"""
mycursor = mydb.cursor()
sql = "INSERT INTO IPL (Team,Matches,Win,Lose,Points) VALUES (%s,%s,%s,%s,%s)"
val = ("Delhi Capitals", "8", "6", "2", "12")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
"""

# Insert Multiple Rows
# To insert multiple rows into a table, use the executemany() method.

"""
mycursor = mydb.cursor()
sql = "INSERT INTO IPL (Team,Matches,Win,Lose,Points) VALUES (%s,%s,%s,%s,%s)"
val = [
  ("Chennai Super Kings", "7", "5", "2", "10"),
  ("Royal Challengers Bangalore", "7", "5", "2", "10"),
  ("Mumbai India", "7", "4", "3", "8"),
  ("Rajasthan Royals", "7", "3", "4", "6"),
  ("Punjab Kings", "8", "3", "5", "6"),
  ("Kolkata Knight Riders", "7", "2", "5", "4"),
  ("Sunrisers Hyderabad", "7", "1", "6", "2"),]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
"""