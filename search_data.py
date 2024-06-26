import json
from search_algorithms.keyword_search import keyword_search
from search_algorithms.semantic_search import semantic_search
from utils.display_results import display_results

# Load configuration
with open('config/config.json', 'r') as file:
    config = json.load(file)

# Extract the search term and search type
search_term = config['search_term']
search_type = config['search_type']
model_name = config.get('model_name', 'bert-base-uncased')  # Default to 'bert-base-uncased' if not specified

# Perform the appropriate search based on config
if search_type == 'keyword':
    hits = keyword_search(search_term)
    display_results(search_term, "Keyword", hits)
elif search_type == 'semantic':
    hits = semantic_search(search_term, model_name)
    display_results(search_term, "Semantic", hits)
else:
    print("Invalid search type specified in config.")
