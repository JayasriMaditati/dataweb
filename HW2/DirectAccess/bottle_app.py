
# Web application for student database (Direct Access)
from bottle import default_app, route,template,get,post,request,redirect
import sqlite3


connection = sqlite3.connect("student.db")
@route('/')
def get_index():
    redirect('/list')

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select * from student")
    rows = list(rows)
    rows = [{"id":row[0],"Firstname":row[1],"Lastname":row[2],"City":row[3]} for row in rows]
    return template('views/student_list.tpl',items = rows )



@get('/add')

def get_add():
     return template('views/add_student.tpl')

@post('/add')
def post_add():
    Firstname = request.forms.get("Firstname")
    Lastname = request.forms.get("Lastname")
    City = request.forms.get("City")
    cursor = connection.cursor()
    cursor.execute(f"insert into student(Firstname,Lastname,City) values('{Firstname}','{Lastname}','{City}')")
    connection.commit()
    redirect('/list')

@get('/delete/<id>') #We can use @route also

def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from student where id = {id}")
    connection.commit()
    redirect('/list')


@get('/edit/<id>')

def get_edit(id):
    cursor = connection.cursor()
    items = cursor.execute(f"select City from student where id= {id}")
    items = list(items)
    if len(items)!=1:
        redirect('/list')
    City = items[0][0]
    return template('views/edit_student.tpl', id = id , City= City)

@post('/edit/<id>')

def post_update(id):
    City = request.forms.get("City")
    cursor = connection.cursor()
    cursor.execute(f"update student set City = '{City}' where id ={id}")
    connection.commit()
    redirect('/list')


application = default_app()

print("done")

