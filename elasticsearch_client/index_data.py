import sys
import os

# Append the project root directory to the system path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from elasticsearch_utils import index_data

if __name__ == "__main__":
    index_data()
