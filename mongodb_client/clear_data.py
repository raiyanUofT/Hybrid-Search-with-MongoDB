from mongodb_client import get_mongodb_client

# Connect to MongoDB
client = get_mongodb_client()

# Connect to the database
db = client['sampledb']

# Drop the collection
db['samplecollection'].drop()

print("Collection 'samplecollection' dropped.")
