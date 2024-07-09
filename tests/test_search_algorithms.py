# FIX THIS DOCUMENT TO CREATE AND DELETE AN 
# ELASTICSEARCH INDEX FOR TESTING PURPOSES

from elasticsearch_client.elasticsearch_client import get_elasticsearch_client
from search_algorithms.keyword_search import keyword_search
from search_algorithms.semantic_search import semantic_search
from search_algorithms.hybrid_search import hybrid_search
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def test_keyword_search():
    documents = [
        {"title": "Test Document 1", "content": "This is a test document."},
        {"title": "Test Document 2", "content": "Another document for testing."}
    ]
    query = "test"
    results = keyword_search(documents, query)
    assert len(results) > 0
    print(f"{Fore.GREEN}Keyword search test succeeded.{Style.RESET_ALL}")

def test_semantic_search():
    documents = [
        {"title": "Test Document 1", "content": "This is a test document."},
        {"title": "Test Document 2", "content": "Another document for testing."}
    ]
    query = "test"
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    results = semantic_search(documents, query, model_name)
    assert len(results) > 0
    print(f"{Fore.GREEN}Semantic search test succeeded.{Style.RESET_ALL}")

def test_hybrid_search():
    documents = [
        {"title": "Test Document 1", "content": "This is a test document."},
        {"title": "Test Document 2", "content": "Another document for testing."}
    ]
    query = "test"
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    results = hybrid_search(documents, query, model_name)
    assert len(results) > 0
    print(f"{Fore.GREEN}Hybrid search test succeeded.{Style.RESET_ALL}")

search_algorithms_tests = {
    "Keyword Search": test_keyword_search,
    "Semantic Search": test_semantic_search,
    "Hybrid Search": test_hybrid_search,
}
