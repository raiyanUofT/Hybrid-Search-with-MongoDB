# Semantic and Keyword Search Project

This project demonstrates how to perform both keyword and semantic search using data stored in MongoDB and indexed into Elasticsearch. The project is modular, making it easy to maintain and extend.

## Functionality

- Insert sample data into MongoDB.
- Clear existing data from MongoDB.
- Index data from MongoDB to Elasticsearch.
- Perform keyword search.
- Perform semantic search using different models.

## Directory Structure

```sh
project/
│
├── config/
│   └── config.json
├── elasticsearch_client/
│   └── elasticsearch_client.py
├── model_loader/
│   └── model_loader.py
├── mongodb_client/
│   ├── mongodb_client.py
│   ├── insert_data.py
│   └── clear_data.py
├── search_algorithms/
│   ├── keyword_search.py
│   └── semantic_search.py
├── utils/
│   └── display_results.py
├── index_data.py
├── insert_data.py
└── search_data.py
```

## Installation

### Pre-Requisites

Python 3.10.12
MongoDB
Elasticsearch

### Install Dependencies

First, ensure you have the required dependencies by installing them from the requirements.txt file:

```sh
pip install -r requirements.txt
```

## Usage

### Steps to Run the Project

2. **Clear existing data from MongoDB**:
    ```sh
    python mongodb_client/clear_data.py
    ```

3. **Insert new data into MongoDB**:
    ```sh
    python mongodb_client/insert_data.py
    ```

4. **Index the new data to Elasticsearch**:
    ```sh
    python index_data.py
    ```

5. **Configure the search parameters** in `config/config.json`:
    ```json
    {
        "search_type": "semantic",  # or "keyword"
        "search_term": "first",
        "model_name": "bert-base-uncased"  # specify the model to be used
    }
    ```

6. **Run the search algorithm**:
    ```sh
    python search_data.py
    ```

## Additional Information

- The `config/config.json` file is used to configure the search type, search term, and model name for semantic search.
