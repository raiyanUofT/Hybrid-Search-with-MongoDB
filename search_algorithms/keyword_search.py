from elasticsearch_client.elasticsearch_client import get_elasticsearch_client

def keyword_search(search_term):
    # Connect to Elasticsearch
    es = get_elasticsearch_client()

    # Define the keyword search query
    search_query = {
        "query": {
            "match": {
                "content": search_term
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
