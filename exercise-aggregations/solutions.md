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
