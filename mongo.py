from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['local']

collenction = db['jerin_collection']

document = {"name":"jerin","age":23,"district":"tvmalai"}

# result = collenction.insert_one(document)
# print(f'document inserted: {result} ')

change = collenction.update_one({"name":"jerin"},{"$set":{"age":24}})
print(f"collection modified_new{change}")