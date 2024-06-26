from elasticsearch_client.elasticsearch_client import get_elasticsearch_client
from model_loader.model_loader import load_model
import torch

def semantic_search(search_term, model_name):
    # Connect to Elasticsearch
    es = get_elasticsearch_client()

    # Load the specified model and tokenizer
    tokenizer, model = load_model(model_name)

    # Encode the search term
    inputs = tokenizer(search_term, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    search_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

    # Prepare the semantic search query
    search_query = {
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'content_vector') + 1.0",
                    "params": {"query_vector": search_embedding.tolist()}
                }
            }
        }
    }

    # Perform the search
    response = es.search(index="sample_index", body=search_query)

    # Extract search results
    hits = response['hits']['hits']

    # Ensure unique hits
    seen_ids = set()
    unique_hits = []
    for hit in hits:
        if hit['_id'] not in seen_ids:
            seen_ids.add(hit['_id'])
            unique_hits.append(hit)

    return unique_hits
