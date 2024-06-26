"""
This module contains tests for verifying MongoDB functionality.

Tests included:
1. test_mongodb_installed: Checks if MongoDB is installed by verifying the version.
    - Pass: MongoDB is installed and the version is retrieved.
    - Fail: MongoDB is not installed or the version command fails.

2. test_mongodb_running: Checks if MongoDB is running by pinging the server.
    - Pass: MongoDB server responds to the ping command.
    - Fail: MongoDB server does not respond or is not running.

3. test_insert_data: Tests the insertion of a document into MongoDB.
    - Pass: Document is successfully inserted and found in the collection.
    - Fail: Document is not found after insertion.

4. test_clear_data: Tests the deletion of a document from MongoDB.
    - Pass: Document is successfully deleted from the collection.
    - Fail: Document is still found after deletion.
"""

import subprocess
from mongodb_client.mongodb_client import get_mongodb_client, get_database, get_collection
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def test_mongodb_installed():
    try:
        subprocess.run(["mongod", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{Fore.GREEN}MongoDB installation test succeeded.{Style.RESET_ALL}")
        return True
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}MongoDB installation test failed.{Style.RESET_ALL}")
        return False

def test_mongodb_running():
    try:
        client = get_mongodb_client()
        client.admin.command('ping')
        print(f"{Fore.GREEN}MongoDB running test succeeded.{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}MongoDB running test failed: {e}{Style.RESET_ALL}")
        return False

def test_insert_data():
    client = get_mongodb_client()
    db = get_database(client)
    collection = get_collection(db)

    # Insert test data
    test_data = {"title": "Test Book", "content": "Test Content"}
    collection.insert_one(test_data)

    # Verify insertion
    inserted_doc = collection.find_one({"title": "Test Book"})
    if inserted_doc:
        print(f"{Fore.GREEN}MongoDB insert data test succeeded.{Style.RESET_ALL}")
        # Clean up
        collection.delete_one({"title": "Test Book"})
        return True
    else:
        print(f"{Fore.RED}MongoDB insert data test failed.{Style.RESET_ALL}")
        return False

def test_clear_data():
    client = get_mongodb_client()
    db = get_database(client)
    collection = get_collection(db)

    # Clean up any existing documents with the same title
    collection.delete_many({"title": "Test Book"})

    # Insert test data
    test_data = {"title": "Test Book", "content": "Test Content"}
    collection.insert_one(test_data)

    # Clear data
    collection.delete_one({"title": "Test Book"})

    # Verify deletion
    remaining_docs = list(collection.find({"title": "Test Book"}))
    if not remaining_docs:
        print(f"{Fore.GREEN}MongoDB clear data test succeeded.{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}MongoDB clear data test failed: Documents not deleted.{Style.RESET_ALL}")
        return False

def test_update_data():
    client = get_mongodb_client()
    db = get_database(client)
    collection = get_collection(db)

    # Insert test data
    test_data = {"title": "Test Book", "content": "Test Content"}
    collection.insert_one(test_data)

    # Update test data
    updated_data = {"$set": {"content": "Updated Content"}}
    collection.update_one({"title": "Test Book"}, updated_data)

    # Verify update
    updated_doc = collection.find_one({"title": "Test Book"})
    if updated_doc and updated_doc["content"] == "Updated Content":
        print(f"{Fore.GREEN}MongoDB update data test succeeded.{Style.RESET_ALL}")
        # Clean up
        collection.delete_one({"title": "Test Book"})
        return True
    else:
        print(f"{Fore.RED}MongoDB update data test failed.{Style.RESET_ALL}")
        return False

def test_retrieve_data():
    client = get_mongodb_client()
    db = get_database(client)
    collection = get_collection(db)

    # Insert test data
    test_data = {"title": "Test Book", "content": "Test Content"}
    collection.insert_one(test_data)

    # Retrieve test data
    retrieved_doc = collection.find_one({"title": "Test Book"})
    if retrieved_doc and retrieved_doc["content"] == "Test Content":
        print(f"{Fore.GREEN}MongoDB retrieve data test succeeded.{Style.RESET_ALL}")
        # Clean up
        collection.delete_one({"title": "Test Book"})
        return True
    else:
        print(f"{Fore.RED}MongoDB retrieve data test failed.{Style.RESET_ALL}")
        return False

# Define all MongoDB test functions
mongodb_tests = {
    "MongoDB Installation": test_mongodb_installed,
    "MongoDB Running": test_mongodb_running,
    "MongoDB Insert Data": test_insert_data,
    "MongoDB Clear Data": test_clear_data,
    "MongoDB Update Data": test_update_data,
    "MongoDB Retrieve Data": test_retrieve_data,
}
