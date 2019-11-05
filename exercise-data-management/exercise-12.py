import json
from elasticsearch import Elasticsearch
import time

# by default we connect to localhost:9200
es = Elasticsearch("http://elasticsearch:9200")

# create an index in elasticsearch, ignore status code 400 (index already exists)
es.indices.delete(index='articles-v1', ignore=[400, 404])
es.indices.create(index='articles-v1', ignore=400)

with open('/code/dataset/articles.json') as json_file:
    data = json.load(json_file)
    start = time.time()
    for idx, article in enumerate(data):
        es.index(index="articles-v1", id=article["Id"], body=article)
        print('Indexed {0} out of {1}'.format(idx + 1, len(data)))

    print('{0} items indexed successfully in {1} seconds!'.format(len(data), time.time() - start))
