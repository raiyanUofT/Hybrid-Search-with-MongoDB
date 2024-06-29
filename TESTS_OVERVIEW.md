# Tests Overview

## Introduction

This document provides an overview of the tests implemented in the project to ensure the functionality of MongoDB and Elasticsearch integrations. Each test verifies a specific aspect of the system, and the results provide insights into the health and correctness of the components.

## Test Files

### `tests/test_mongodb.py`

This file contains tests for verifying MongoDB functionality.

- **test_mongodb_installed**: Verifies that MongoDB is installed by checking the version.
  - **Pass**: MongoDB is installed and the version is retrieved.
  - **Fail**: MongoDB is not installed or the version command fails.

- **test_mongodb_running**: Verifies that MongoDB is running by pinging the server.
  - **Pass**: MongoDB server responds to the ping command.
  - **Fail**: MongoDB server does not respond or is not running.

- **test_insert_data**: Tests the insertion of a document into MongoDB.
  - **Pass**: Document is successfully inserted and found in the collection.
  - **Fail**: Document is not found after insertion.

- **test_clear_data**: Tests the deletion of a document from MongoDB.
  - **Pass**: Document is successfully deleted from the collection.
  - **Fail**: Document is still found after deletion.

### `tests/test_elasticsearch.py`

This file contains tests for verifying Elasticsearch functionality.

- **test_elasticsearch_installed**: Verifies that Elasticsearch is installed by pinging the server.
  - **Pass**: Elasticsearch server responds to the ping command.
  - **Fail**: Elasticsearch server does not respond or is not installed.

- **test_elasticsearch_running**: Verifies that Elasticsearch is running by pinging the server.
  - **Pass**: Elasticsearch server responds to the ping command.
  - **Fail**: Elasticsearch server does not respond or is not running.

- **test_create_index**: Tests the creation of an index in Elasticsearch.
  - **Pass**: Index is successfully created and exists.
  - **Fail**: Index is not created or does not exist.

- **test_index_document**: Tests the indexing of a document in Elasticsearch.
  - **Pass**: Document is successfully indexed and retrievable.
  - **Fail**: Document is not found after indexing.

- **test_search_document**: Tests the search functionality in Elasticsearch.
  - **Pass**: Document is successfully found using search query.
  - **Fail**: Document is not found using search query.

- **test_delete_document**: Tests the deletion of a document from Elasticsearch.
  - **Pass**: Document is successfully deleted and not retrievable.
  - **Fail**: Document is still found after deletion.

## Running the Tests

To run all the tests, navigate to the project root directory and execute the following command:

```sh
export PYTHONPATH=$(pwd)
python tests/run_tests.py
```