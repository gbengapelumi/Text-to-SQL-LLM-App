import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert, record, create table, retrieve
cursor = connection.cursor()

## create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)

"""

cursor.execute(table_info)

##Insert Some more records

cursor.execute("""Insert Into STUDENT values('GBENGA', 'Data Science', 'A', 90)""")
cursor.execute("""Insert Into STUDENT values('DUNSIN', 'Data Science', 'B', 100)""")
cursor.execute("""Insert Into STUDENT values('FEMI', 'Data Science', 'A', 86)""")
cursor.execute("""Insert Into STUDENT values('TOLANI', 'DEVOPS', 'A', 50)""")
cursor.execute("""Insert Into STUDENT values('MITCHELL', 'DEVOPS', 'A', 35)""")

##Display all the records
print("The inserted records are")

data = cursor.execute("""Select *  From STUDENT""")

for row in data:
    print(row)


## Close the connection

connection.commit()
connection.close()