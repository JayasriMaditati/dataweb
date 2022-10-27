from peewee import SqliteDatabase,Model,CharField

db = SqliteDatabase('peewee_shopping_list.db')

class Item(Model):
    description = CharField()
    class Meta:
        database = db


def get_items(id=None):
    if id == None:
        items = Item.select()
    else:
        items = Item.select().where(Item.id==int(id))
    items = [{'id':item.id,'description':item.description} for item in items]
    return items

def add_items(description):
    Item.create(description=description)

def delete_items(id):
    q = Item.delete().where(Item.id==int(id))
    q.execute()

def update_items(id, description):
    q = Item.update({Item.description:description}).where(Item.id == int(id))
    q.execute()
