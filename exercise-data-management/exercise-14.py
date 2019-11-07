from elasticsearch import Elasticsearch
from time import strftime, localtime, mktime, sleep, time

es = Elasticsearch("http://elasticsearch:9200")
end = time() + 5 * 60
print(end)

while ((end - time()) > 0):
    now = localtime()
    es.index(index='logs-{0}'.format(strftime("%Y-%m-%d-%H-%M", now)), body={'timestamp': mktime(now), 'message': 'XYZ'})
    print('Indexed new document into {}'.format('logs-{0}'.format(strftime("%Y-%m-%d-%H-%M", now))))
    sleep(5)
