"""
This module contains tests for verifying Elasticsearch functionality.

Tests included:
1. test_elasticsearch_installed: Checks if Elasticsearch is installed by pinging the server.
    - Pass: Elasticsearch server responds to the ping command.
    - Fail: Elasticsearch server does not respond or is not installed.

2. test_elasticsearch_running: Checks if Elasticsearch is running by pinging the server.
    - Pass: Elasticsearch server responds to the ping command.
    - Fail: Elasticsearch server does not respond or is not running.

3. test_create_index: Tests the creation of an index in Elasticsearch.
    - Pass: Index is successfully created and exists.
    - Fail: Index is not created or does not exist.

4. test_index_document: Tests the indexing of a document in Elasticsearch.
    - Pass: Document is successfully indexed and retrievable.
    - Fail: Document is not found after indexing.

5. test_search_document: Tests the search functionality in Elasticsearch.
    - Pass: Document is successfully found using search query.
    - Fail: Document is not found using search query.

6. test_delete_document: Tests the deletion of a document from Elasticsearch.
    - Pass: Document is successfully deleted and not retrievable.
    - Fail: Document is still found after deletion.
"""

import subprocess
from elasticsearch_client.elasticsearch_client import get_elasticsearch_client
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def test_elasticsearch_installed():
    # Check if Elasticsearch client can be imported and used
    try:
        es = get_elasticsearch_client()
        es.ping()
        print(f"{Fore.GREEN}Elasticsearch installation test succeeded.{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}Elasticsearch installation test failed: {e}{Style.RESET_ALL}")
        return False

def test_elasticsearch_running():
    try:
        es = get_elasticsearch_client()
        es.ping()
        print(f"{Fore.GREEN}Elasticsearch running test succeeded.{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}Elasticsearch running test failed: {e}{Style.RESET_ALL}")
        return False

def test_create_index():
    es = get_elasticsearch_client()
    index_name = 'test_index'

    # Clean up any pre-existing index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    try:
        es.indices.create(index=index_name)
        if es.indices.exists(index=index_name):
            print(f"{Fore.GREEN}Elasticsearch create index test succeeded.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Elasticsearch create index test failed.{Style.RESET_ALL}")
            return False
    finally:
        es.indices.delete(index=index_name)

def test_index_document():
    es = get_elasticsearch_client()
    index_name = 'test_index'
    document = {"title": "Test Document", "content": "Test content for Elasticsearch."}

    # Clean up any pre-existing index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    try:
        es.indices.create(index=index_name)
        es.index(index=index_name, id=1, document=document)
        indexed_doc = es.get(index=index_name, id=1)
        if indexed_doc['_source'] == document:
            print(f"{Fore.GREEN}Elasticsearch index document test succeeded.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Elasticsearch index document test failed.{Style.RESET_ALL}")
            return False
    finally:
        es.indices.delete(index=index_name)

def test_search_document():
    es = get_elasticsearch_client()
    index_name = 'test_index'
    document = {"title": "Test Document", "content": "Test content for Elasticsearch."}

    # Clean up any pre-existing index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    try:
        es.indices.create(index=index_name)
        es.index(index=index_name, id=1, document=document)
        es.indices.refresh(index=index_name)
        search_result = es.search(index=index_name, query={"match": {"title": "Test Document"}})
        if search_result['hits']['total']['value'] > 0:
            print(f"{Fore.GREEN}Elasticsearch search document test succeeded.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Elasticsearch search document test failed.{Style.RESET_ALL}")
            return False
    finally:
        es.indices.delete(index=index_name)

def test_delete_document():
    es = get_elasticsearch_client()
    index_name = 'test_index'
    document = {"title": "Test Document", "content": "Test content for Elasticsearch."}

    # Clean up any pre-existing index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    try:
        es.indices.create(index=index_name)
        es.index(index=index_name, id=1, document=document)
        es.delete(index=index_name, id=1)
        es.indices.refresh(index=index_name)
        try:
            es.get(index=index_name, id=1)
            print(f"{Fore.RED}Elasticsearch delete document test failed.{Style.RESET_ALL}")
            return False
        except Exception:
            print(f"{Fore.GREEN}Elasticsearch delete document test succeeded.{Style.RESET_ALL}")
            return True
    finally:
        es.indices.delete(index=index_name)

def test_update_document():
    es = get_elasticsearch_client()
    index_name = 'test_index'
    document = {"title": "Test Document", "content": "Test content for Elasticsearch."}
    updated_document = {"doc": {"content": "Updated content for Elasticsearch."}}

    # Clean up any pre-existing index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    try:
        es.indices.create(index=index_name)
        es.index(index=index_name, id=1, document=document)
        es.update(index=index_name, id=1, body=updated_document)
        updated_doc = es.get(index=index_name, id=1)
        if updated_doc['_source']['content'] == "Updated content for Elasticsearch.":
            print(f"{Fore.GREEN}Elasticsearch update document test succeeded.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Elasticsearch update document test failed.{Style.RESET_ALL}")
            return False
    finally:
        es.indices.delete(index=index_name)

def test_bulk_indexing():
    es = get_elasticsearch_client()
    index_name = 'test_index'
    documents = [
        {"index": {"_index": index_name, "_id": 1}},
        {"title": "Test Document 1", "content": "Content 1"},
        {"index": {"_index": index_name, "_id": 2}},
        {"title": "Test Document 2", "content": "Content 2"},
    ]

    # Clean up any pre-existing index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    try:
        es.indices.create(index=index_name)
        es.bulk(body=documents)
        es.indices.refresh(index=index_name)
        doc1 = es.get(index=index_name, id=1)
        doc2 = es.get(index=index_name, id=2)
        if doc1['_source']['title'] == "Test Document 1" and doc2['_source']['title'] == "Test Document 2":
            print(f"{Fore.GREEN}Elasticsearch bulk indexing test succeeded.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Elasticsearch bulk indexing test failed.{Style.RESET_ALL}")
            return False
    finally:
        es.indices.delete(index=index_name)

def test_delete_index():
    es = get_elasticsearch_client()
    index_name = 'test_index'

    # Ensure index exists
    es.indices.create(index=index_name, ignore=400)

    try:
        es.indices.delete(index=index_name)
        if not es.indices.exists(index=index_name):
            print(f"{Fore.GREEN}Elasticsearch delete index test succeeded.{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Elasticsearch delete index test failed.{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}Elasticsearch delete index test failed: {e}{Style.RESET_ALL}")
        return False

# Define all Elasticsearch test functions
elasticsearch_tests = {
    "Elasticsearch Installed": test_elasticsearch_installed,
    "Elasticsearch Running": test_elasticsearch_running,
    "Elasticsearch Create Index": test_create_index,
    "Elasticsearch Index Document": test_index_document,
    "Elasticsearch Search Document": test_search_document,
    "Elasticsearch Delete Document": test_delete_document,
    "Elasticsearch Update Document": test_update_document,
    "Elasticsearch Bulk Indexing": test_bulk_indexing,
    "Elasticsearch Delete Index": test_delete_index,
}
