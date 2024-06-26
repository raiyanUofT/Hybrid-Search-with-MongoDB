from pymongo import MongoClient

def get_mongodb_client():
    return MongoClient('mongodb://localhost:27017/')
