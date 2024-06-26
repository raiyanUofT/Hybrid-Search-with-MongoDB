from elasticsearch import Elasticsearch

def get_elasticsearch_client():
    return Elasticsearch('http://localhost:9200')
