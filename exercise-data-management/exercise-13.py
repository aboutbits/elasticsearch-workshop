import json
from elasticsearch import Elasticsearch
import time

# by default we connect to localhost:9200
es = Elasticsearch("http://elasticsearch:9200")

# create an index in elasticsearch, ignore status code 400 (index already exists)
es.indices.delete(index='articles-v2', ignore=[400, 404])
es.indices.create(index='articles-v2', ignore=400)

with open('/code/dataset/articles.json') as json_file:
    data = json.load(json_file)
    body = []
    start = time.time()
    for article in data:
        body.append({'index': {'_index': 'articles-v2', '_type': 'doc', '_id': article['Id']}})
        body.append(article)
    
    es.bulk(body=body)

    print('{0} items indexed successfully in {1} seconds!'.format(len(data), time.time() - start))
