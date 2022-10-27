import dataset

db = dataset.connect("sqlite:///student.db")

try:
    db['student'].drop()
except:
    pass

db.begin()
try:
    table = db['student']
    rows = [
            {"Firstname":'Jayasri',"Lastname":'Maditati',"City":'Cleveland'},
            {"Firstname":'Tom',"Lastname":'keen',"City":'Texas'},
            {"Firstname":'Rajesh',"Lastname":'Krish',"City":'Cleveland'},
            {"Firstname":'Jennifer',"Lastname":'Ann',"City":'LA'},
            {"Firstname":'Kristin',"Lastname":'Summer',"City":'Orlando'}
            ]

    table.insert_many(rows)
    db.commit()
except:
    db.rollback()

print("done")



