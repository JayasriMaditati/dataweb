
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,template,get,post,request,redirect

import Database


@route('/')

def get_index():
    redirect('/list')

@route('/list')
def get_list():
    items = Database.get_items()
    return template('Views/shopping_list.tpl',shopping_list = items )


@post('/add')
def post_add():
    description = request.forms.get("description")
    Database.add_items(description)
    redirect('/list')

@get('/delete/<id>') #We can use @route also

def get_delete(id):
    Database.delete_items(id)
    redirect('/list')


@get('/edit/<id>')

def get_edit(id):
    items = Database.get_items(id)
    if len(items)!=1:
        redirect('/list')
    item_id, description = items[0]['id'],items[0]['desc']
    assert item_id == int(id)
    #return f"{[item_id]}{[id]}"
    return template('Views/edit_item.tpl', id = id ,description=description)

@post('/edit/<id>')

def post_edit(id):
    description = request.forms.get("description")
    Database.update_items(id,description)
    redirect('/list')


application = default_app()

print("done")