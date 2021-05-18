import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")

"""
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Playoffs (Standing INT AUTO_INCREMENT PRIMARY KEY, Team VARCHAR(255), Matches INT, Win INT, Lose INT, Points INT)")

mycursor = mydb.cursor()
sql = "INSERT INTO Playoffs (Team,Matches,Win,Lose,Points) VALUES (%s,%s,%s,%s,%s)"
val = [
  ("Delhi Capitals", "8", "6", "2", "12")
  ("Chennai Super Kings", "7", "5", "2", "10"),
  ("Royal Challengers Bangalore", "7", "5", "2", "10"),
  ("Mumbai India", "7", "4", "3", "8")]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
"""


print("----------------Join Two or More Tables----------------")


# A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
                            # Different types of SQL Joins:
# -> (INNER) JOIN: Returns records that have matching values in both tables.
# -> LEFT (OUTER) JOIN: Returns all records from the left table,and the matched records from the right table.
# -> RIGHT (OUTER) JOIN: Returns all records from the right table,and the matched records from left table.

# (INNER) JOIN -> select * from _First_Table_Name_ JOIN _Second_Table_Name_ ON _First_Table_Name_.id = _Second_Table_Name.id;
# LEFT (OUTER) JOIN -> SELECT column_name FROM table1 LEFT JOIN table2 ON table1.column_name = table2column_name;
# RIGHT (OUTER) JOIN -> SELECT column_name FROM table1 Right JOIN table2 ON table1.column_name = table2column_name;

print("--------------------INNER JOIN--------------------")

mycursor = mydb.cursor()
sql = "SELECT \
      IPL.Team AS IPL, \
      Playoffs.Team AS Team \
      FROM IPL \
      INNER JOIN Playoffs ON IPL.Team = Playoffs.Team"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("--------------------LEFT JOIN--------------------")

mycursor = mydb.cursor()
sql = "SELECT \
      IPL.Team AS IPL, \
      Playoffs.Team AS Team \
      FROM IPL \
      LEFT JOIN Playoffs ON IPL.Team = Playoffs.Team"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("--------------------Right JOIN--------------------")

mycursor = mydb.cursor()
sql = "SELECT \
      IPL.Team AS IPL, \
      Playoffs.Team AS Team \
      FROM IPL \
      RIGHT JOIN Playoffs ON IPL.Team = Playoffs.Team"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)