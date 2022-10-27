from peewee import SqliteDatabase,Model,CharField

db = SqliteDatabase('peewee_student.db')

class Student(Model):
    Firstname = CharField()
    Lastname = CharField()
    City = CharField()
    class Meta:
        database = db

def add_student_db():
    global db
    rows = [
        {"Firstname":'Jayasri',"Lastname":'Maditati',"City":'Cleveland'},
        {"Firstname":'Tom',"Lastname":'keen',"City":'Texas'},
        {"Firstname":'Rajesh',"Lastname":'Krish',"City":'Cleveland'},
        {"Firstname":'Jennifer',"Lastname":'Ann',"City":'LA'},
        {"Firstname":'Kristin',"Lastname":'Summer',"City":'Orlando'}
         ]
    for row in rows:
        Student.create(Firstname = row['Firstname'],Lastname = row['Lastname'],City = row['City'])


if __name__ == "__main__":
    db.connect()
    db.create_tables([Student])
    add_student_db()

print("done")