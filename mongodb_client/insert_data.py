from mongodb_client import get_mongodb_client

# Connect to MongoDB
client = get_mongodb_client()

# Create or connect to a database
db = client['sampledb']

# Create or connect to a collection
collection = db['samplecollection']

# Sample data
documents = [
    {"title": "Document 1", "content": "This is the content of the first document."},
    {"title": "Document 2", "content": "This is the content of the second document."},
    {"title": "Document 3", "content": "This is the content of the third document."}
]

# Insert sample data
collection.insert_many(documents)

print("Sample data inserted into MongoDB.")
