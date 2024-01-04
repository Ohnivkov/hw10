import json
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
db = client["hw8"]
with open('quotes.json','r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for qoute in quotes:
    author = db.authors.find_one({'fullname': qoute['author']})
    if author:
        db.quotes.insert_one({
            'quote': qoute['quote'],
            'tags': qoute['tags'],
            'author':ObjectId(author['_id'])
        })