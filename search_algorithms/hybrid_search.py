from search_algorithms.keyword_search import keyword_search
from search_algorithms.semantic_search import semantic_search
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize_scores(results, new_min=0, new_max=2):
    if not results:
        return results
    scores = np.array([doc['_score'] for doc in results]).reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(new_min, new_max))
    normalized_scores = scaler.fit_transform(scores).flatten()
    for doc, normalized_score in zip(results, normalized_scores):
        doc['_score'] = normalized_score
    return results

def hybrid_search(query, model_name):
    # Perform keyword search
    keyword_results = keyword_search(query)

    # Perform semantic search
    semantic_results = semantic_search(query, model_name)
    
    # Normalize the scores
    keyword_results = normalize_scores(keyword_results)
    
    # Combine results, ensuring uniqueness
    combined_results = {doc['_id']: doc for doc in keyword_results + semantic_results}
    unique_hits = list(combined_results.values())
    
    # Optionally sort the results by some relevance criteria
    # For example, you could add scores from both searches if available
    # sorted(unique_hits, key=lambda x: x.get('score', 0), reverse=True)

    # Sort results by normalized score
    sorted_unique_hits = sorted(unique_hits, key=lambda x: x['_score'], reverse=True)

    return sorted_unique_hits
