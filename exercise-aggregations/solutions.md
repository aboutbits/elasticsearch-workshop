# Solutions

## Exercise 2 - Metric Aggregations

```json
GET /accommodations/_search
{
  "query": {
    "match_all": {}
  },
  "aggs": {
    "sum_beds": {
      "sum": {
        "field": "Beds"
      }
    },
    "arerage_beds": {
      "avg": {
        "field": "Beds"
      }
    },
    "min_beds": {
      "min": {
        "field": "Beds"
      }
    },
    "max_beds": {
      "max": {
        "field": "Beds"
      }
    }
  }
}
```

## Exercise 3 - Bucket Aggregations

1. term aggregation

```json
GET /accommodations/_search
{
  "query": {
    "match_all": {}
  },
  "aggs": {
    "categories": {
      "terms": {
        "field": "AccoCategoryId",
        "size": 20
      }
    }
  }
}
```

2. size

https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html#search-aggregations-bucket-terms-aggregation-size

3. query

```json
GET /accommodations/_search
{
  "query": {
    "multi_match": {
      "query": "Gröden",
      "fields": [
        "LocationInfo.RegionInfo.Name.*",
        "LocationInfo.DistrictInfo.Name.*",
        "LocationInfo.MunicipalityInfo.Name.*"
      ]
    }
  },
  "aggs": {
    "categories": {
      "terms": {
        "field": "AccoCategoryId",
        "size": 20
      }
    }
  }
}
```

## Exercise 4 - Bucket and Metric Aggregations

```json
GET /accommodations/_search
{
  "query": {
    "match_all": {}
  },
  "aggs": {
    "categories": {
      "terms": {
        "field": "AccoCategoryId",
        "size": 20
      },
      "aggs": {
        "sum_beds": {
          "sum": {
            "field": "Beds"
          }
        },
        "arerage_beds": {
          "avg": {
            "field": "Beds"
          }
        },
        "min_beds": {
          "min": {
            "field": "Beds"
          }
        },
        "max_beds": {
          "max": {
            "field": "Beds"
          }
        }
      }
    }
  }
}
```
