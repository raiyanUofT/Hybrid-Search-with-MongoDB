import json
from mongodb_client import get_mongodb_client

# Connect to MongoDB
client = get_mongodb_client()

# Create or connect to a database
db = client['sampledb']

# Create or connect to a collection
collection = db['samplecollection']

# Clear existing data
collection.drop()

# Load sample data from JSON file
with open('mongodb_client/books_data.json', 'r') as file:
    documents = json.load(file)

# Insert sample data
collection.insert_many(documents)

print("Sample data inserted into MongoDB.")
