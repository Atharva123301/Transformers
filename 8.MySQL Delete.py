import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="athved@123",
    database="MyDatabase")


print("----------------Delete Record----------------")


# You can delete records from an existing table by using the "Delete From" statement:

# Delete any record where the team is "Mumbai Indians":

"""
mycursor = mydb.cursor()
sql = "DELETE FROM IPL WHERE Team = 'Mumbai Indians'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
"""

# Important

'Important!: Notice the statement: mydb.commit(). It is required to make the changes,'\
' otherwise no changes are made to the table.'

'Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) '
'that should be deleted. If you omit the WHERE clause, all records will be deleted!'


print("----------------Prevent SQL Injection----------------")


#It is considered a good practice to escape the values of any query, also in delete statements.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#The mysql.connector module uses the placeholder %s to escape values in the delete statement:

#Escape values by using the placeholder %s method:

"""
mycursor = mydb.cursor()
sql = "DELETE FROM IPL WHERE Team = %s"
adr = ("Mumbai Indians", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
"""