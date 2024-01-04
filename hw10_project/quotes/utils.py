from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
    db = client["hw8"]
    return db