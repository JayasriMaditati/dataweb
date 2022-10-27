from mongita import MongitaClientDisk
client = MongitaClientDisk()

from bson.objectid import ObjectId

# Creating a Hello_world_db Database

Hello_world_db_1 = client.Hello_world_db_1

#In Database, we will create a collection.A collection is a grouping of MongoDB documents. 
# Documents within a collection can have different fields. A collection is the equivalent of a table in a relational database system.
#  A collection exists within a single database.

mongoose_collection = Hello_world_db_1.mongoose_collection

#Now we have to insert documents

mongoose_collection.insert_many([{'name':'Meercat','does_not_eat':'snakes'},
                                {'name':'Yello Mongoose','eats':'Termites'}])
                                
print(" docs:", mongoose_collection.count_documents({}))

print(list(mongoose_collection.find({})))

print("____ updated contents_____")

mongoose_collection.update_one({'name':'Meercat'},{'$set':{'weight':2}})

print(list(mongoose_collection.find({'weight':2})))

mongoose_collection.update_one({'weight':{'$gt':1}},{'$set':{'weight':4}})
print(list(mongoose_collection.find({'weight':{'$gt':1}})))

print("____ deleted contents_____")
mongoose_collection.delete_one({'weight':{'$gt':1}})
print(list(mongoose_collection.find({})))