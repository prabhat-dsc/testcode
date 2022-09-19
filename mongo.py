import pymongo

client = pymongo.MongoClient("mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
