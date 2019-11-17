# Exercises

## Exercise 1 - Fetch & Import Dataset

First, you have to fetch the dataset and import all the data into Elasticsearch if you haven't done this before. We prepared already these scripts for you. Just execute the following scripts.

```bash
docker-compose run --rm python python dataset/fetch.py
docker-compose run --rm python python exercise-search/import.py
```

## Exercise 2 - Match All Query

Execute a `match_all` on the the index `articles`. How many articles are in the index?

## Exercise 3 - Specifying Search Index

Execute a `match_all` query on the following indices:

- All indices in the cluster
- The indices `articles` and `activities`
- All indices starting with "a"

How many results do you find with the different queries?

## Exercise 4 - Term Queries

1. Find all items in the index `articles` where the field `Type` is "buchtippartikel".
2. Find all items in the index `articles` where the field `HasLanguage` contains "de" or "it".
2. Find all items in the index `articles` where the field `HasLanguage` contains "de" and "it".

## Exercise 5 - From and Size

Find all items in the index `articles` where the field `Type` is "presseartikel", but only return the items form 100 to 150.

## Exercise 6 - Range Queries

1. Find all items in the index `articles` where the field `ArticleDate` is not older than five years.
2. Find all items in the index `activities` where the field `Difficulty` is between 1 and 3.

## Exercise 7 - Match Queries

1. Run a search query to find items in the index `articles` where the field `Detail.de.Title` matches the text "Südtirol".
2. Run a search query to find items in the index `articles` where the field `Detail.de.Title` matches the text "Südtirol Urlaub". For this query one of the words should be in the title, but not both have to.
3. Why are there more results for the second query compared to the first query?
4. Run a search query to find items in the index `articles` where the field `Detail.de.Title` matches the text "Südtirol Urlaub". For this query both words should be in the title.
5. Run a search query to find items in the index `articles` where the field `Detail.de.Title` matches the text "Südtirol Urlaub Bauernhof". For this query two words should be in the title.

## Exercise 8 - Multi Match Queries

1. Run a search query to find items in the index `articles` where the fields `Detail.de.Title` and `Detail.de.BaseText` matches the text "Südtirol Wein".
1. Run a search query to find items in the index `articles` where the fields `Detail.de.Title` and `Detail.de.BaseText` matches the text "Südtirol Wein". Give also the field `Detail.de.Title` an extra boost of 2.

## Exercise 9 - Bool Queries

1. Search all items in the index `articles` where the field `Type` is "basisartikel". In addition, also filter all items that have the languages "de" (`HasLanguage`).
2. Enhance the first query by returning only items where the field `Active` is not "false".
3. Search all items in the index `accommodations` with the following requirements:
    - Search for the place "Gröden" in the fields `LocationInfo.RegionInfo.Name.*`, `LocationInfo.DistrictInfo.Name.*` and `LocationInfo.MunicipalityInfo.Name.*``
    - Filter accommodations with `AccoTypeId` as "HotelPension"
    - Filter accommodations with `AccoCategoryId` as "5stars"
    - And optionally rank accommodations higher if the have "Schwimmbad" or "Sauna" as a feature in `Features.Name`

## Exercise 10 - Explain

Run the following query and analyze the explanation of Elasticsearch how they calculate the score.

```json
GET /articles/_search
{
  "explain": true,
  "query": {
    "bool": {
      "must": {
        "match": {
          "Detail.de.Title": {
            "query": "Südtirol Wein"
          }
        }
      },
      "filter": {
        "term": {
          "Type": {
            "value": "basisartikel"
          }
        }
      } 
    }
  }
}
```


