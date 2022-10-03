
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,template,get,post,request,redirect

from dataset_Database import get_items,add_items,update_items,delete_items


@route('/')

def get_index():
    redirect('/list')

@route('/list')
def get_list():
    items = get_items()
    return template('Views/shopping_list.tpl',shopping_list = items )


@post('/add')
def post_add():
    description = request.forms.get("description")
    quantity = request.forms.get("quantity")
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    add_items(description,quantity)
    redirect('/list')

@get('/delete/<id>') #We can use @route also

def get_delete(id):
    delete_items(id)
    redirect('/list')


@get('/edit/<id>')

def get_edit(id):
    items = get_items(id)
    if len(items)!=1:
        redirect('/list')
    item_id, description = items[0]['id'],items[0]['description']
    assert item_id == int(id)
    #return f"{[item_id]}{[id]}"
    return template('Views/edit_item.tpl', id = id ,description=description)

@post('/edit/<id>')

def post_edit(id):
    description = request.forms.get("description")
    update_items(id,description)
    redirect('/list')


application = default_app()

print("done")