# Solutions

## Exercise 1 - Global Analyze API and Built-in Analyzers

Standard Analyzer:

```json
POST _analyze
{
  "analyzer": "standard",
  "text": "The 4 programmers are thinking about new interesting features that they should implement using XP."
}
```

Simple Analyzer:

```json
POST _analyze
{
  "analyzer": "simple",
  "text": "The 4 programmers are thinking about new interesting features that they should implement using XP."
}
```

Whitespace Analyzer:

```json
POST _analyze
{
  "analyzer": "whitespace",
  "text": "The 4 programmers are thinking about new interesting features that they should implement using XP."
}
```

Stop Analyzer:

```json
POST _analyze
{
  "analyzer": "stop",
  "text": "The 4 programmers are thinking about new interesting features that they should implement using XP."
}
```

## Exercise 2 - Index Analyzer API and Custom Analyzers

1. Create index

```json
PUT /text-analysis-2
{
  "settings": {
    "analysis": {
      "analyzer": {
        "message_analyzer": {
          "char_filter": ["html_strip"],
          "tokenizer": "standard",
          "filter": ["lowercase"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "username": {
        "type": "text",
        "analyzer": "message_analyzer"
      }
    }
  }
}
```

2. Analyze by referencing the analyzer

```json
POST /text-analysis-2/_analyze
{
  "analyzer": "message_analyzer",
  "text": "The <b>CUSTOM</b> analyzers are awesome!"
}
```

3. Analyze by referencing the field

```json
POST /text-analysis-2/_analyze
{
  "field": "message",
  "text": "The <b>CUSTOM</b> analyzers are awesome!"
}
```

## Exercise 3 - Custom Analyzer with Synonyms and Stopwords

1. Create index

```json
PUT /text-analysis-3
{
  "settings": {
    "analysis": {
      "filter": {
        "english_stopwords": {
          "type": "stop",
          "stopwords": "_english_"
        },
        "custom_synonyms": {
          "type": "synonym",
          "synonyms" : [
            ":) => happy",
            ":( => sad"
          ]
        }
      },
      "analyzer": {
        "message_analyzer": {
          "tokenizer": "whitespace",
          "filter": ["english_stopwords", "custom_synonyms"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "username": {
        "type": "text",
        "analyzer": "message_analyzer"
      }
    }
  }
}
```

2. Analyze the text

```json
POST /text-analysis-3/_analyze
{
  "analyzer": "message_analyzer",
  "text": "Today is a new day and I'm so :)"
}
```

## Exercise 4 - Custom Analyzer with NGrams

1. Create index

```json
PUT /text-analysis-4
{
  "settings": {
    "analysis": {
      "filter": {
        "trigrams": {
          "type": "ngram",
          "min_gram" : 3,
          "max_gram": 3
        }
      },
      "analyzer": {
        "message_analyzer": {
          "tokenizer": "standard",
          "filter": ["lowercase", "trigrams"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "username": {
        "type": "text",
        "analyzer": "message_analyzer"
      }
    }
  }
}
```

2. Analyze the text

```json
POST /text-analysis-4/_analyze
{
  "analyzer": "message_analyzer",
  "text": "Apfelsaft ohne Zusatzstoffe"
}
```

## Exercise 5 - Language Analyzers

English Language Analyzer:

https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-lang-analyzer.html#english-analyzer

```json
POST _analyze
{
  "analyzer": "english",
  "text": "..."
}
```

German Language Analyzer:

https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-lang-analyzer.html#german-analyzer

```json
POST _analyze
{
  "analyzer": "german",
  "text": "..."
}
```

Italian Language Analyzer:

https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-lang-analyzer.html#italian-analyzer

```json
POST _analyze
{
  "analyzer": "italian",
  "text": "..."
}
```
