import os

# Configuration settings for MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = 'sampledb'
COLLECTION_NAME = 'samplecollection'
