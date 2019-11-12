import json
from elasticsearch import Elasticsearch

def import_dataset(name, file_name, index_name):
    es = Elasticsearch(["elasticsearch"])

    es.indices.delete(index=index_name, ignore_unavailable=True)
    # es.indices.create(index=index_name, body={
    #     'mappings': {
    #         'properties': {
    #             'Type': {
    #                 'type': 'keyword'
    #             }
    #         }
    #     }
    # })

    with open(file_name) as file:
        items = json.load(file)

        for item in items:
            es.index(index=index_name, id=item['Id'], body=item)

        print('{0}: {1} items imported'.format(name, len(items))) 


import_dataset('Activities', 'dataset/activities.json', 'activities')
import_dataset('Articles', 'dataset/articles.json', 'articles')
