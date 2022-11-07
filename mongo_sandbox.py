from pymongo import MongoClient

import json
with open("private.json","r") as f:
    private = json.load(f)

password = private["mongo"]
print(password)

client = MongoClient(f"mongodb+srv://Example_user:{password}@cluster0.g85qpbj.mongodb.net/?retryWrites=true&w=majority")


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