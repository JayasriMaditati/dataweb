import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

rows = cursor.execute("select * from list")
rows = list(rows)



#List comprehension

# x = [1,2,3]
# print([-k for k in x])
# print([{"zz":-k} for k in x])
# print([{"pos":k,"neg":-k} for k in x])
# print([{"pos":k,"neg":-k,"dbl":2*k} for k in x])
# print([{"pos":k,"neg":-k,"dbl":2*k} for k in x if k>1])
rows = [{"id":row[0],"desc":row[1]} for row in rows]
print(rows)