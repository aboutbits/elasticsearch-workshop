# Exercises

## Exercise 1 - Fetch & Import Dataset

First, you have to fetch the dataset and import all the data into Elasticsearch if you haven't done this before. We prepared already these scripts for you. Just execute the following scripts.

```bash
docker-compose run --rm python python dataset/fetch.py
docker-compose run --rm python python dataset/import.py
```

## Exercise 2 - Metric Aggregations

Try to find out what the total, the average, the minimum and the maximum number of beds (field `Beds`) in the index `accommodations` is.


## Exercise 3 - Bucket Aggregations

Try to group the accommodations in the index `accommodations` into groups of their category (field `AccoCategoryId`). How many accommodations exist in the different groups?

Why are no all categories defined when you don't specify a size parameter? Why are all categories listed when you specify a size of 20?

## Exercise 4 - Bucket and Metric Aggregations

Try to find out what the total, the average, the minimum and the maximum number of beds (field `Beds`) for every bucket is that you receive from the query of exercise 3.
