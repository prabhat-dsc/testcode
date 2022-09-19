import  pymongo
client = pymongo.MongoClient("mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":'ravi',
    "surname":'teja',
    "job":'Big data'
}
d={
    "name":'prabhat',
    "surname":"singh",
    "job":'datascience'
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)