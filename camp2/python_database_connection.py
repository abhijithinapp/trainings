#SQL Connection
from sqlite3 import Row
import pyodbc

#create a connection string
conString = 'Driver={SQL Server};Server=CPU1213\SQLEXPRESS;Database=pythondb;Trusted_Connection=yes;'
myconn = pyodbc.connect(conString)
myCursor = myconn.cursor()

try:     
    myCursor.execute('''CREATE TABLE employee(
        id INT IDENTITY PRIMARY KEY,
        name VARCHAR(50),
        age SMALLINT ,
        location VARCHAR(50)
        )''')
except Exception as e:
    print("Cannot create the table")
    print(f"{type(e).__name__} was occured,")
    print(e)


myconn.commit()
myCursor.execute('''SELECT * FROM employee''')
employees = [{'empcode' : row[0], 'empname': row[1], 'age':row[2], 'location': row[3]} for row in myCursor.fetchall()]
print(employees)
myconn.close()

