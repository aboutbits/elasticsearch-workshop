# Solutions

## Exercise 2 - Match All Query

```json
GET /articles/_search
{
  "query": {
    "match_all": {}
  }
}
```

## Exercise 3 - Specifying Search Index

```json
GET /_search
{
  "query": {
    "match_all": {}
  }
}
```

```json
GET /articles,activities/_search
{
  "query": {
    "match_all": {}
  }
}
```

```json
GET /a*/_search
{
  "query": {
    "match_all": {}
  }
}
```

## Exercise 4 - Term Queries

1. Term Query

```json
GET /articles/_search
{
  "query": {
    "term": {
      "Type": {
        "value": "buchtippartikel"
      }
    }
  }
}
```

2. Terms Query

```json
GET /articles/_search
{
  "query": {
    "terms": {
      "HasLanguage": ["de", "it"]
    }
  }
}
```

3. Terms Set Query

```json
GET /articles/_search
{
  "query": {
    "terms_set": {
      "HasLanguage": {
        "terms": ["de", "it"],
        "minimum_should_match_script": {
          "source": "2"
        }
      }
    }
  }
}
```

## Exercise 5 - From and Size

```json
GET /articles/_search
{
  "from": 100,
  "size": 50,
  "query": {
    "term": {
      "Type": {
        "value": "presseartikel"
      }
    }
  }
}
```

## Exercise 6 - Range Queries

1. Date Range

```json
GET /articles/_search
{
  "query": {
    "range": {
      "ArticleDate": {
        "gt": "now-5y"
      }
    }
  }
}
```

2. Integer Range

```json
GET /activities/_search
{
  "query": {
    "range": {
      "Difficulty": {
        "gte": 1,
        "lte": 3
      }
    }
  }
}
```

## Exercise 7 - Match Queries

1. "Südtirol"

```json
GET /articles/_search
{
  "query": {
    "match": {
      "Detail.de.Title": {
        "query": "Südtirol"
      }
    }
  }
}
```

2. "Südtirol Urlaub" (operator: or)

```json
GET /articles/_search
{
  "query": {
    "match": {
      "Detail.de.Title": {
        "query": "Südtirol Urlaub"
      }
    }
  }
}
```

4. "Südtirol Urlaub" (operator: and)

```json
GET /articles/_search
{
  "query": {
    "match": {
      "Detail.de.Title": {
        "query": "Südtirol Urlaub",
        "operator": "and"
      }
    }
  }
}
```

5. "Südtirol Urlaub Bauernhof" (minimum_should_match: 2)

```json
GET /articles/_search
{
  "query": {
    "match": {
      "Detail.de.Title": {
        "query": "Südtirol Urlaub Bauernhof",
        "minimum_should_match": "2"
      }
    }
  }
}
```

## Exercise 8 - Multi Match Queries

1. "Wein Eisacktal"

```json
GET /articles/_search
{
  "query": {
    "multi_match": {
      "query": "Wein Eisacktal",
      "fields": ["Detail.de.Title", "Detail.de.BaseText"]
    }
  }
}
```

2. "Wein Eisacktal" (Boost the field `Detail.de.Title`)

```json
GET /articles/_search
{
  "query": {
    "multi_match": {
      "query": "Wein Eisacktal",
      "fields": ["Detail.de.Title^2", "Detail.de.BaseText"]
    }
  }
}
```

## Exercise 9 - Bool Queries

1. must and filter

```json
GET /articles/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "Type": {
              "value": "basisartikel"
            }
          }
        }
      ],
      "filter": [
        {
          "term": {
            "HasLanguage": {
              "value": "de"
            }
          }
        }
      ]
    }
  }
}
```

2. must_not

```json
GET /articles/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "Type": {
              "value": "basisartikel"
            }
          }
        }
      ],
      "filter": [
        {
          "term": {
            "HasLanguage": {
              "value": "de"
            }
          }
        }
      ],
      "must_not": [
        {
          "term": {
            "Active": {
              "value": false
            }
          }
        }
      ]
    }
  }
}
```

3. should

```json
GET /accommodations/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "multi_match": {
            "query": "Gröden",
            "fields": [
              "LocationInfo.RegionInfo.Name.*",
              "LocationInfo.DistrictInfo.Name.*",
              "LocationInfo.MunicipalityInfo.Name.*"
            ]
          }
        }
      ],
      "filter": [
        {
          "term": {
            "AccoTypeId": {
              "value": "HotelPension"
            }
          }
        },
        {
          "term": {
            "AccoCategoryId": {
              "value": "5stars"
            }
          }
        }
      ],
      "should": [
        {
          "term": {
            "Features.Name": {
              "value": "Schwimmbad"
            } 
          }
        },
        {
          "term": {
            "Features.Name": {
              "value": "Sauna"
            } 
          }
        }
      ]
    }
  }
}
```
