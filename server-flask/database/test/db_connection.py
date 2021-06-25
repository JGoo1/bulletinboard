from pymongo import MongoClient, ReturnDocument

host="localhost"
port="27017"
client = MongoClient(host, int(port))

db_name="bulletinboard"
collection_name="counters"

query = { "_id": "replyid"}
update = { "$inc": { "seq": 1}}

res = client[db_name][collection_name].find_and_modify(query=query, update=update,
                                                       return_document=ReturnDocument.AFTER)

print(res)