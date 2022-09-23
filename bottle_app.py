
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,template,get,post,request,redirect
import sqlite3

connection = sqlite3.connect("shopping_list.db")


@route('/')
def hello_world():
    return 'Hello from jayasri!'

@route('/hi')
def hi_world():
    return 'Hi from jayasri!'

@route('/bye')
def bye_world():
    return 'bye from jayasri!'


@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select * from list")
    rows = list(rows)
    rows = [{"id":row[0],"desc":row[1]} for row in rows]
    return template('Views/shopping_list.tpl',items = rows )


@get('/add')

def get_add():
    return template('Views/add_item.tpl')

@post('/add')
def post_add():
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"insert into list(description) values('{description}')")
    connection.commit()
    redirect('/list')

@get('/delete/<id>') #We can use @route also

def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id = {id}")
    connection.commit()
    redirect('/list')


@get('/edit/<id>')

def get_edit(id):
    cursor = connection.cursor()
    items = cursor.execute(f"select description from list where id= {id}")
    items = list(items)
    if len(items)!=1:
        redirect('/list')
    description = items[0][0]
    return template('Views/edit_item.tpl', id = id ,description=description)

@post('/edit/<id>')

def post_update(id):
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"update list set description = '{description}' where id ={id}")
    connection.commit()
    redirect('/list')


application = default_app()

print("done")