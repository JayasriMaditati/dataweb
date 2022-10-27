import sqlite3

connection = sqlite3.connect("student.db")

def get_list(id=None):
    cursor = connection.cursor()
    if id:
        rows = cursor.execute(f"select * from student where id= {id}")
    else:
        rows = cursor.execute("select * from student")
    rows = list(rows)
    rows = [{"id":row[0],"Firstname":row[1],"Lastname":row[2],"City":row[3]} for row in rows]
    return rows


def test_get_list():
    print("testing get list of students")
    rows = get_list()
    assert type(rows) is list
    assert len(rows) > 0
    assert type(rows[0]) is dict
    assert 'id' in rows[0].keys()
    assert 'Firstname' in rows[0].keys()
    assert type(rows[0]['id']) is int
    assert type(rows[0]['City']) is str
    pass


def add_student(Firstname,Lastname,City):
    cursor = connection.cursor()
    cursor.execute(f"insert into student(Firstname,Lastname,City) values('{Firstname}','{Lastname}','{City}')")
    connection.commit()

import time

def random_string():
    return str(time.time())


def test_add_student():
    print("Testing Add Students")
    Firstname = random_string()
    Lastname = random_string()
    City = random_string()
    add_student(Firstname,Lastname,City)
    rows = get_list()
    row = rows[-1]
    assert City == row['City']


def delete_student(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from student where id = {id}")
    connection.commit()

def test_delete_student():
    print("testing delete students")
    Firstname = random_string()
    Lastname = random_string()
    City = random_string()
    add_student(Firstname,Lastname,City)
    rows = get_list()
    row = rows[-1]
    assert City == row['City']
    delete_student(row['id'])
    rows = get_list()
    for row in rows:
        assert City != row['City']

def update_city(id,City):
    cursor = connection.cursor()
    cursor.execute(f"update student set City = '{City}' where id ={id}")
    connection.commit()

def test_update_city():
    print("testing Update students")
    Firstname = random_string()
    Lastname = random_string()
    City = random_string()
    add_student(Firstname,Lastname,City)
    rows = get_list()
    row = rows[-1]
    id = str(row['id'])
    City = row['City']
    new_city = City.replace("1","9").replace(".",":")
    update_city(id,new_city)
    rows = get_list()
    new_found = False
    for row in rows:
        if row['id'] == int(id):
            assert row['City'] == new_city
            new_found = True
        assert row['City'] != City
    assert new_found

if  __name__ == "__main__":
    test_get_list()
    test_add_student()
    test_delete_student()
    test_update_city()
    print("done")