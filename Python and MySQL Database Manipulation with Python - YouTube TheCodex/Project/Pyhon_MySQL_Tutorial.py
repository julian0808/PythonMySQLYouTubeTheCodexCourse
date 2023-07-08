import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='',
    database='testdb',
)

# print(mydb)

mycursor = mydb.cursor()


# Deleting Entries and Dropping Tables


#Delete a table

sql = "DROP TABLE students"

mycursor.execute(sql)

mydb.commit()


#Delete a single record
# sql = "DELETE FROM students WHERE name = 'Rachel' "
#
# mycursor.execute(sql)
#
# mydb.commit()

# Ordering our Queries and Results

# sql = "SELECT * FROM students ORDER BY age DESC"
# sql = "SELECT * FROM students ORDER BY name DESC"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for r in myresult:
#     print(r)

# Updating Entries and Limiting Queries

# sql = "UPDATE students SET age = 13 WHERE name = 'Bob'"

# mycursor.execute(sql)

# mydb.commit()

# mycursor.execute("SELECT * FROM students LIMIT 5")
# mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")
#
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)







# Query Conditions with WHERE and Wildcards

# sql = "SELECT * FROM students WHERE name='Rachel'"
# sql = "SELECT * FROM students WHERE name = %s"
#
# mycursor.execute(sql , ("Rachel", ))
#
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)

#  Selecting and Getting Data

# specific table:
# mycursor.execute("SELECT age FROM students")

# mycursor.execute("SELECT * FROM students")

# myresult = mycursor.fetchall()
# myresult = mycursor.fetchone()
#
#
# for row in myresult:
#     print(row)



# How to ppulating our Database and Table


# sqlFormula = "INSERT INTO students(name, age) VALUES (%s, %s)"
# student1 = ("Rachel", 22)

# students = [("Bob", 12),
#             ("Amanda", 32),
#             ("Jacob", 21),
#             ("Avi", 28),
#             ("Michelle", 17),]

# mycuror.executemany(sqlFormula, students)
#
# mydb.commit()


# Create database
# mycursor.execute("CREATE DATABASE testdb")

# mycursor.execute("SHOW DATABASES")
#
# for db in mycursor:
#     print(db)

# Create table

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")
#
# for tb in mycursor:
#     print(tb)




