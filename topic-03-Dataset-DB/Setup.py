import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list(id integer primary key, description text)")

cursor.execute("insert into list(description) values ('apples')")
cursor.execute("insert into list(description) values ('brocolli')")
cursor.execute("insert into list(description) values ('burger')")
cursor.execute("insert into list(description) values ('fruits')")
cursor.execute("insert into list(description) values ('veggies')")

connection.commit()
connection.close()

print("done")