import json
from search_algorithms.keyword_search import keyword_search
from search_algorithms.semantic_search import semantic_search
from search_algorithms.hybrid_search import hybrid_search
from utils.display_results import display_results
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load configuration
with open('config/config.json', 'r') as file:
    config = json.load(file)

# Extract the search term and search type
search_term = config['search_term']
search_type = config['search_type']
model_name = config.get('model_name', 'sentence-transformers/all-MiniLM-L6-v2')  # Default to 'sentence-transformers/all-MiniLM-L6-v2' if not specified

# Perform the appropriate search based on config
if search_type == 'keyword':
    print(f"{Fore.BLUE}{Style.BRIGHT}Performing keyword search for term: '{search_term}'{Style.RESET_ALL}")
    hits = keyword_search(search_term)
    display_results(search_term, "Keyword", hits)
elif search_type == 'semantic':
    print(f"{Fore.BLUE}{Style.BRIGHT}Performing semantic search for term: '{search_term}' using model '{model_name}'{Style.RESET_ALL}")
    hits = semantic_search(search_term, model_name)
    display_results(search_term, "Semantic", hits)
elif search_type == 'hybrid':
    print(f"{Fore.BLUE}{Style.BRIGHT}Performing hybrid search for term: '{search_term}' using model '{model_name}'{Style.RESET_ALL}")
    hits = hybrid_search(search_term, model_name)
    display_results(search_term, "Hybrid", hits)
else:
    print(f"{Fore.RED}{Style.BRIGHT}Invalid search type specified in config.{Style.RESET_ALL}")
