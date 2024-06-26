from mongodb_client.mongodb_client import get_mongodb_client
from elasticsearch_client.elasticsearch_client import get_elasticsearch_client
from elasticsearch.helpers import bulk
from model_loader.model_loader import load_model
import torch

# Connect to MongoDB
client = get_mongodb_client()
db = client['sampledb']
collection = db['samplecollection']

# Connect to Elasticsearch
es = get_elasticsearch_client()

# Load BERT model and tokenizer
tokenizer, model = load_model('bert-base-uncased')

# Fetch data from MongoDB
documents = collection.find()

# Prepare data for bulk indexing
actions = []

for doc in documents:
    # Encode the content
    inputs = tokenizer(doc['content'], return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    content_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

    action = {
        "_index": "sample_index",
        "_source": {
            "title": doc["title"],
            "content": doc["content"],
            "content_vector": content_embedding.tolist()
        }
    }
    actions.append(action)

# Index data to Elasticsearch
bulk(es, actions)

print("Data indexed into Elasticsearch with dense vectors.")
