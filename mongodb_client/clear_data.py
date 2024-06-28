from mongodb_client import get_mongodb_client, get_database, get_collection
from config_mongodb_client import COLLECTION_NAME
from colorama import init, Fore, Style

# Connect to MongoDB
client = get_mongodb_client()
db = get_database(client)
collection = get_collection(db)

# Clear existing data
collection.drop()

print(f"{Fore.RED}{Style.BRIGHT}Collection '{COLLECTION_NAME}' dropped.{Style.RESET_ALL}")
