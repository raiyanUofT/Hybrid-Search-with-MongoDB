from pymongo import MongoClient
from .config_mongodb_client import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

def get_mongodb_client():
    """Get a MongoDB client."""
    return MongoClient(MONGODB_URI)

def get_database(client):
    """Get the database."""
    return client[DATABASE_NAME]

def get_collection(db):
    """Get the collection."""
    return db[COLLECTION_NAME]
