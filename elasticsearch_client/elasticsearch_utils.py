import sys
import os

# Append the project root directory to the system path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from model_loader.model_loader import load_model
from elasticsearch_client import get_elasticsearch_client
from config.config_utils import get_model_name
import torch

def setup_index(index_name="sample_index"):
    es = get_elasticsearch_client()

    # Load the specified model and tokenizer
    model_name = get_model_name()
    tokenizer, model = load_model(model_name)

    # Extract the dimension from the model
    inputs = tokenizer("example", return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    dimensions = outputs.last_hidden_state.shape[-1]

    # Delete the existing index if it exists
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    
    # Create the index with the correct mapping
    mapping = {
        "mappings": {
            "properties": {
                "title": {
                    "type": "text"
                },
                "content": {
                    "type": "text"
                },
                "content_vector": {
                    "type": "dense_vector",
                    "dims": dimensions  # Set this dynamically
                }
            }
        }
    }

    es.indices.create(index=index_name, body=mapping)
    print(f"Elasticsearch index '{index_name}' created with dense vector dimensions: {dimensions}")

    return tokenizer, model

def index_data(index_name="sample_index"):
    from mongodb_client.mongodb_client import get_mongodb_client
    from elasticsearch.helpers import bulk

    # Ensure the Elasticsearch index is set up correctly
    tokenizer, model = setup_index(index_name)

    # Connect to MongoDB
    client = get_mongodb_client()
    db = client['sampledb']
    collection = db['samplecollection']

    # Connect to Elasticsearch
    es = get_elasticsearch_client()

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
            "_index": index_name,
            "_source": {
                "title": doc["title"],
                "content": doc["content"],
                "content_vector": content_embedding.tolist()
            }
        }
        actions.append(action)

    # Index data to Elasticsearch
    bulk(es, actions)

    print(f"Data indexed into Elasticsearch index '{index_name}' with dense vectors.")
