import dataset

db = dataset.connect("sqlite:///student.db")

def get_list(id=None):
    table = db['student']
    if id:
        rows = table.find(id = int(id))
    else:
        rows = table.find()
    rows = [dict(row) for row in rows]
    return rows


def add_student(Firstname,Lastname,City):
    db.begin()
    try:
        table = db['student']
        row = {"Firstname":Firstname,"Lastname":Lastname,"City":City}
        table.insert(row)
        db.commit()
    except:
        db.rollback()


def delete_student(id):
    db.begin()
    try:
        table = db['student']
        table.delete(id=int(id))
        db.commit()
    except:
        db.rollback()



def update_city(id,City):
    db.begin()
    try:
        table = db['student']
        new_data = {'id':int(id), 'City':City}
        table.update(new_data, ['id'])
        db.commit()
    except:
        db.rollback()

