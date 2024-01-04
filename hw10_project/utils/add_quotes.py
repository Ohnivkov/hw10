import json
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
db = client["hw8"]
with open('quotes.json','r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    print(author)
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author':ObjectId(author['_id'])
        })