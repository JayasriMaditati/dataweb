# Database.py - function for Managing Database

import sqlite3

connection = sqlite3.connect("shopping_list.db")

def get_items(id=None):
    cursor = connection.cursor()
    if id:
        items = cursor.execute(f"select id,description from list where id= {id}")
    else:
        items = cursor.execute("select id,description from list")
    items = list(items)
    items = [{"id":item[0],"desc":item[1]} for item in items]
    return items



def add_items(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into list(description) values('{description}')")
    connection.commit()




def delete_items(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id = {id}")
    connection.commit()




def update_items(id,description):
    cursor = connection.cursor()
    cursor.execute(f"update list set description = '{description}' where id ={id}")
    connection.commit()





#Now to test the above functions externally , the below module runs directly instead of being run as library

# if  __name__ == "__main__":
#     test_get_items()
#     test_add_items()
#     test_delete_items()
#     test_update_items()
#     print("done")