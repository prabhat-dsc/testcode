import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['mydb']
collection = database['invetory']
data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]
# collection.insert_many(data)
# d=collection.find({'item':{'$gt':'p'}})
# d=collection.find({'status':'D'})
# d=collection.find({'status':{'$in':['A',"P"]}})
# d=collection.find({'$or':[{'status':'A'},{'status':'D'}]})
#d = collection.find({'qty': {'$lte': 50},'status':'A'})
#d = collection.find({'qty': 100,'size.h':28})
#d = collection.find({'qty':{'$gte':50},'size.h':{'$gt':15}})
#d = collection.find({'$or':[{'status':'A'},{'status':'P'}],'qty':25})
#d=collection.find({'$or':[{'qty':{'$gt':50}},{'status':'A'}],'size.h':{'$gt':15}})
#d=collection.update_one({'item':'canvas'},{'$set':{'item':'prabhat'}})
#collection.delete_one({"item": 'prabhat'})
d=collection.find()
for i in d:
    print(i)
