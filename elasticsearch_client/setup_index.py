import sys
import os

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from elasticsearch_utils import setup_index

if __name__ == "__main__":
    setup_index()
