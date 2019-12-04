import pymongo

client = pymongo.MongoClient('localhost')
db = client['test']
db['test'].insert({
    'name':'didi'
})
info = db['test'].find_one({
    'name':'wei'
})
print(info)