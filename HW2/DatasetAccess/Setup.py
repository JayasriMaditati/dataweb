import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table student")
except:
    pass

cursor.execute("create table student(id integer primary key, Firstname text, Lastname text, City text)")

cursor.execute("insert into student(Firstname,Lastname,City) values ('Jayasri','Maditati','Ohio')")
cursor.execute("insert into student(Firstname,Lastname,City) values ('Tom','Keen','Texas')")
cursor.execute("insert into student(Firstname,Lastname,City) values ('Tim','David','Texas')")
cursor.execute("insert into student(Firstname,Lastname,City) values ('Angel','Liz','NY')")


connection.commit()
connection.close()
