import requests
import json

def fetch(name, url, filename):
    items = []
    page = 1
    size = 500

    while True:
        response = requests.get('{0}?pagenumber={1}&pagesize={2}'.format(url, page, size))

        if response.status_code != 200:
            print('Failed to fetch {0}'.format(name))
            exit(-1)

        data = response.json()

        items.extend(data['Items'])

        if data['CurrentPage'] == data['TotalPages']:
            break

        page = page + 1

    with open(filename, 'w') as file:
        json.dump(items, file)

    print('{0}: {1} items fetched'.format(name, len(items)))

fetch('Accommodations', 'https://tourism.opendatahub.bz.it/api/Accommodation', 'accommodations.json')
fetch('Activities', 'https://tourism.opendatahub.bz.it/api/Activity', 'activities.json')
fetch('Articles', 'https://tourism.opendatahub.bz.it/api/Article', 'articles.json')
fetch('Events', 'https://tourism.opendatahub.bz.it/api/Event', 'events.json')
