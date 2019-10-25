import requests
import json

def fetch_dataset(name, url, file_name):
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

    with open(file_name, 'w') as file:
        json.dump(items, file)

    print('{0}: {1} items fetched'.format(name, len(items)))

fetch_dataset('Accommodations', 'https://tourism.opendatahub.bz.it/api/Accommodation', 'dataset/accommodations.json')
fetch_dataset('Activities', 'https://tourism.opendatahub.bz.it/api/Activity', 'dataset/activities.json')
fetch_dataset('Articles', 'https://tourism.opendatahub.bz.it/api/Article', 'dataset/articles.json')
fetch_dataset('Events', 'https://tourism.opendatahub.bz.it/api/Event', 'dataset/events.json')
