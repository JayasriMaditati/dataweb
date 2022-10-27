from peewee import SqliteDatabase,Model,CharField

db = SqliteDatabase('peewee_student.db')

class Student(Model):
    Firstname = CharField()
    Lastname = CharField()
    City = CharField()
    class Meta:
        database = db

def get_list(id=None):
    if id == None:
        rows = Student.select()
    else:
        rows = Student.select().where(Student.id==int(id))
    rows = [{'id':row.id,'Firstname':row.Firstname,'Lastname':row.Lastname,'City':row.City} for row in rows]
    return rows

def add_student(Firstname,Lastname,City):
    Student.create(Firstname=Firstname,Lastname=Lastname,City=City)

def delete_student(id):
    q = Student.delete().where(Student.id==int(id))
    q.execute()

def update_city(id, City):
    q = Student.update({Student.City:City}).where(Student.id == int(id))
    q.execute()