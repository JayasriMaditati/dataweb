
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,template
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

application = default_app()

print("done")