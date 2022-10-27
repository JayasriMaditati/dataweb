
# Web application using DB abstraction layer - Dataset  Database
from bottle import default_app, route,template,get,post,request,redirect

from student_dataset import get_list,add_student,delete_student,update_city

@route('/')


def get_index():
    redirect('/list')

@route('/list')
def get_student():
    rows = get_list()
    return template('views/student_list.tpl',items = rows )



@get('/add')

def get_add():
     return template('views/add_student.tpl')

@post('/add')
def post_add():
    Firstname = request.forms.get("Firstname")
    Lastname = request.forms.get("Lastname")
    City = request.forms.get("City")
    add_student(Firstname,Lastname,City)
    redirect('/list')

@get('/delete/<id>') #We can use @route also

def get_delete(id):
    delete_student(id)
    redirect('/list')


@get('/edit/<id>')

def get_edit(id):
    rows = get_list(id)
    if len(rows)!=1:
        redirect('/list')
    row_id, City = rows[0]['id'],rows[0]['City']
    assert row_id == int(id)
    return template('views/edit_student.tpl', id = id , City= City)

@post('/edit/<id>')

def post_update(id):
    City = request.forms.get("City")
    update_city(id,City)
    redirect('/list')


application = default_app()

print("done")

