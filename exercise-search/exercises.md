# Exercises

## Exercise 1 - Fetch & Import Dataset

First, you have to fetch the dataset and import all the data into Elasticsearch. We prepared already these scripts for you. Just execute the following scripts.

```bash
docker-compose run --rm python python dataset/fetch.py
docker-compose run --rm python python exercise-search/import.py
```

GET /_search
GET /articles/_search
GET /articles,activities/_search
GET /a*/_search
