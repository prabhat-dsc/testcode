import pymongo
client = pymongo.MongoClient("mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
mydb=client['info']  # database
collection=mydb['products']   # table/collection
print('collection created')
## insert list of records
list_of_record=[
    {"pid":101,"pname":'table',"price":100},
    {"pid":102,"pname":'chair',"price":120},
    {"pid":103,"pname":'mobile',"price":200},
    {"pid":104,"pname":'book',"price":80},{"pid":105,"pname":'pen',"price":75},
]
collection.insert_many(list_of_record)
print('records inserted')
## fetch all data
records=collection.find()
for i in records:
    print(i)