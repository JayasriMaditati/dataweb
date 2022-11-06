from mongita import MongitaClientDisk
client = MongitaClientDisk()

from bson.objectid import ObjectId

student_db = client.student_db
student_collection = student_db.student_collection


def get_list(id=None):
    if id == None:
        rows = student_collection.find()
    else:
        rows = student_collection.find({'_id':ObjectId(id)})
    rows = [{'id':str(row['_id']),'Firstname':row['Firstname'],'Lastname':row['Lastname'],'City':row['City']} for row in rows]
    return rows

def add_student(Firstname,Lastname,City):
    student_collection.insert_one({'Firstname':Firstname,'Lastname':Lastname,'City':City})

def delete_student(id):
    student_collection.delete_one({'_id':ObjectId(id)})


def update_city(id, City):
    student_collection.update_one({'_id':ObjectId(id)},{'$set':{'City':City}})
