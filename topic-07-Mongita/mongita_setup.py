from mongita import MongitaClientDisk
client = MongitaClientDisk()

from bson.objectid import ObjectId

student_db = client.student_db
student_collection = student_db.student_collection

student_collection.delete_many({})

student_collection.insert_many([
        {"Firstname":'Jayasri',"Lastname":'Maditati',"City":'Cleveland'},
        {"Firstname":'Tom',"Lastname":'keen',"City":'Texas'},
        {"Firstname":'Rajesh',"Lastname":'Krish',"City":'Cleveland'},
        {"Firstname":'Jennifer',"Lastname":'Ann',"City":'LA'},
        {"Firstname":'Kristin',"Lastname":'Summer',"City":'Orlando'}
    ])


items = list(student_collection.find({}))

print(items)

print("done")