import pymongo
# establish connection with mongodb atlas
client = pymongo.MongoClient("mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
## create database
database=client['info']
collection=database['myinfo']
## insert data to collection
data={
    "name":'prabhat',
    "surname":'singh',
    "job":'datascience',
    "city":'hyd'
}
collection.insert_one(data)
## insert another data with diff schema
data1={"name":'ram','contact':123445,"sal":100}
collection.insert_one(data1)
## fetch all info
record=collection.find()
for i in record:
    print(i)