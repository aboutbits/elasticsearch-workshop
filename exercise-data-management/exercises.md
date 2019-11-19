# Exercises

## Exercise 1 - Open Kibana and go to Dev Tools

Dev Tools allow us to make REST API calls to our Elasticsearch cluster, with syntax highlighting and autocompletion. Please open Kibana Dev Tools by clicking on this [link](http://localhost:5601/app/kibana#/dev_tools/console?_g=()).

Now execute the following request to see all indexes in our cluster.

```
GET /_cat/indices
```

You should get something like this:

```
green open .kibana_task_manager_1   WuZ62aQ8RFmbv8tbZ1-1lA 1 0 2 0 12.5kb 12.5kb
green open .apm-agent-configuration kKwMZUyvQIqWNxE7svncNQ 1 0 0 0   283b   283b
green open .kibana_1                1gw4PIjKQr-ICJW3D1ta9A 1 0 9 3 43.5kb 43.5kb
```

This are internal indexes that are used by kibana itself.

To list all indices in the UI you can go to [Index management](http://localhost:5601/app/kibana#/management?_g=()).
The internal indices are not shown in this UI.

## Exercise 2 - Index a document

Lets create our first index, by simply indexing a document. We **do not** create an index upfront.

```
POST /events-v1/_doc/
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C85", 
    "Type": "1", 
    "Active": true, 
    "Title": "100. Giro d'Italia: Start der 19. Etappe Innichen - Piancavallo" 
  }
```

You should get a response from Elasticsearch that contains a field `_id`. Although we have a field in the request body `Id` Elasticsearch created its own id for this document.

Lets check the indexes again with the request or in [Index management](http://localhost:5601/app/kibana#/management?_g=()).

```
GET /_cat/indices
```

You should now see a new index with the name `events-v1`. And it has exactly one document in it.

## Exercise 3 - Index a few more documents

Please take the example from exercise 2, modify the body a little bit and index them. Lets add 2 more documents.

```
POST /events-v1/_doc/
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C84", 
    "Type": "1", 
    "Active": true, 
    "Title": "100. Giro d'Italia: Start der 16. Etappe Bozen - Bruneck"
  }
```

```
POST /events-v1/_doc/
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C83", 
    "Type": "1", 
    "Active": true, 
    "Title": "100. Giro d'Italia: Start der 17. Etappe Bruneck - Sterzing"
  }
```

## Exercise 4 - Retrieve our documents

We again have two options to see our documents in an index.
Lets first query Elasticsearch directly:

```
GET /events-v1/_search
```

The second approach uses Kibana do it in the UI. Open the following [link](http://localhost:5601/app/kibana#/management/kibana/index_patterns?_g=()) to manage index patterns.
Click on the blue button in the right top corner **Create index pattern**.

You should see a form, that asks you to enter an index pattern. Please enter the index name in this field. In our case it is `events-v1`. Click on **Next step** and then on **Create index pattern**.

Now you can navigate to the [Discover tab](http://localhost:5601/app/kibana#/discover?_g=()).

In this view you should see all 3 documents, that have been added in the previous steps.

## Exercise 5 - Update a document

In order to do a full document replacement we need to know the `_id` of the document. For that purpose please copy the `_id` and the body of one of our documents into the following command:

```
PUT /events-v1/_doc/<COPY DOCUMENT ID>
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C85", 
    "Type": "1", 
    "Active": false,
    "Title": "100. Giro d'Italia: Start der 19. Etappe Innichen - Piancavallo" 
  }
```

The document will be replaced completely. If you skip fields, they will be removed. For example if we remove `type` from the body, it will delete the field from the document.

```
PUT /events-v1/_doc/<COPY DOCUMENT ID>
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C85", 
    "Active": false,
    "Title": "100. Giro d'Italia: Start der 19. Etappe Innichen - Piancavallo" 
  }
```

Check the changes in the [Discover tab](http://localhost:5601/app/kibana#/discover?_g=()) or with search API.

## Exercise 6 - Update a single field in a document

Lets use the single field update API to add the delete field again.

```
POST /events-v1/_update/<COPY DOCUMENT ID>
{
    "doc" : {
        "Type": "1"
    }
}
```

Check the changes in the [Discover tab](http://localhost:5601/app/kibana#/discover?_g=()) or with search API.

## Exercise 7 - Try to insert a document with a wrong datatype

Try to insert the following document.

```
POST /events-v1/_doc/
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C83", 
    "Type": "1", 
    "Active": "Active", 
    "Title": "100. Giro d'Italia: Start der 17. Etappe Bruneck - Sterzing"
  }
```

We will get a mapping error containing the following message.

```json
"type": "mapper_parsing_exception",
"reason": "failed to parse field [Active] of type [boolean] in document with id 'IKw9PG4BOXgyEKN59-kD'. Preview of field's value: 'Active'"
```

We tried to index a document with a string value for the Active field, but it should be a boolean value. Why is it like that? We never specified any mapping for this index. Elasticsearch dynamically creates a mapping for every new field in an index.

Use the following request to check the mapping for our `events-v1` index.

```
GET /events-v1/_mapping
```

You should see that the data type for `Active` is boolean. All other fields are of the same type:

```
"type" : "text",
"fields" : {
    "keyword" : {
      "type" : "keyword",
      "ignore_above" : 256
    }
  }
```

This mapping means that Elasticsearch is internally creating two fields for a single value, that we can use to search on. e.g. `Title` and `Title.keyword`

```
GET /events-v1/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "Title": "Bozen"
          }
        }
      ]
    }
  }
}
```

We can do a full text query on the `Title` field, because it is indexed as text.

And we can do an exact term query or aggregations on the `Title.keyword` field.

```
GET /events-v1/_search
{
  "query": {
    "term": {
      "Title.keyword": {
        "value": "100. Giro d'Italia: Start der 16. Etappe Bozen - Bruneck"
      }
    }
  }
}
```

Further details about filtering and full text searches will be covered later.

## Exercise 8 - Create a new index with predefined mapping

In this exercise we will create the index before we start indexing to have a more optimal mapping. For example on the `Id` field we do not need full text search capabilities. Whereas on the `Title` field we don't need term filters.

Lets create a new more optimal index `events-v2`.

```
PUT /events-v2
{
  "mappings": {
    "properties": {
      "Id": {
        "type": "keyword"
      },
      "Title": {
        "type": "text"
      }
    }
  }
}
```

Check the mapping:

```
GET /events-v2/_mapping
```

Now lets add again a document:

```
POST /events-v2/_doc/
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C85", 
    "Type": "1", 
    "Active": true, 
    "Title": "100. Giro d'Italia: Start der 19. Etappe Innichen - Piancavallo" 
  }
```

Check again the mapping:

```
GET /events-v2/_mapping
```

Now you should see that Elasticsearch added the mapping for `Active` and `Type` automatically. 

## Exercise 9 - Index Templates

You do not always want to define all fields upfront, but you would like to have a different default behavior. We can use index templates to define a default setting for certain data types.

For our new index, we want that every string should just be specified as keyword. This keeps the memory footprint small and if we really need full text search, than we can define it explicitly.

Lets create a new index again:

```
PUT /events-v3
{
  "mappings": {
    "properties": {
      "Title": {
        "type": "text"
      }
    }, 
    "dynamic_templates": [
      {
        "strings_as_keywords": {
          "match": "*",
          "match_mapping_type": "string",
          "mapping": {
            "type": "keyword"
          }
        }
      }
    ]
  }
}
```

With this setup every field that gets added and is a string will be of type `keyword`, except `Title`.

Lets try it out:

```
POST /events-v3/_doc/
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C85", 
    "Type": "1", 
    "Active": true, 
    "Title": "100. Giro d'Italia: Start der 19. Etappe Innichen - Piancavallo" 
  }
```

Check the mapping:

```
GET /events-v3/_mapping
```

Now we should have no double mappings per field anymore and the default is for strings is `keyword`.

## Exercise 10 - Change mapping of a field and reindex

Lets try to change the mapping of the `Type` field from `keyword` to `integer`.

```
PUT /events-v3/_mapping
{
  "properties": {
    "Type": {
      "type": "integer"
    }
  }
}
```

If we try to do this Elasticsearch will complain as it doesn't allow us to change the type of a field from `keyword` to `integer`.

We need to create a new index and reindex all data.

```
PUT /events-v4
{
  "mappings": {
    "properties": {
      "Title": {
        "type": "text"
      },
      "Type": {
        "type": "integer"
      }
    }, 
    "dynamic_templates": [
      {
        "strings_as_keywords": {
          "match": "*",
          "match_mapping_type": "string",
          "mapping": {
            "type": "keyword"
          }
        }
      }
    ]
  }
}
```

Lets reindex all documents (in our case 1 document) from `events-v3` to `events-v4`.

```
POST _reindex
{
  "source": {
    "index": "events-v3"
  },
  "dest": {
    "index": "events-v4"
  }
}
```

Check that the documents have been reindex and check the mapping.

```
GET /events-v4/_search
```

```
GET /events-v4/_mapping
```

## Exercise 11 - Create an alias

With the exercise before we created a new index `events-v4`, but all our applications are still pointing to `events-v3`.
We would now have to go to each application, change the code and redeploy. Quite painful and error prone, if you forget one. Aliases can help in such scenarios. We will create an alias called `events` and point it to the current index. We change our application code to point to `events` and in the future, if we ever have to create a new version of the events index, we can simply point the alias to that index and our applications continue to work as before.

```
POST /_aliases
{
  "actions": [
    {
      "add": {
        "index": "events-v4",
        "alias": "events"
      }
    }
  ]
}
```

Try to query the newly created alias.

```
GET /events/_search
```

Try yourself to point the alias to `events-v1`. Be careful to not make it point to 2 indices at the same time.

## Exercise 12 - Indexation with single document API

In this exercise we are going to index the `articles.json` dataset.
We will index each document at a time.

Open your terminal and execute the `exercise-12.py` python script.

```bash
docker-compose run --rm python python exercise-data-management/exercise-12.py
```

Please take note on how long it took.

Also open [Index management](http://localhost:5601/app/kibana#/management?_g=()) and check the size of the index.

## Exercise 13 - BULK index API

In this exercise we want to improve the speed of indexation and reduce the memory footprint.
For this reason we will make use of the BULK API.

Open your terminal and execute the `exercise-13.py` python script.

```bash
docker-compose run --rm python python exercise-data-management/exercise-12.py
```

Please take note on how long it took and compare it to the results from exercise 12.

Open again [Index management](http://localhost:5601/app/kibana#/management?_g=()) and check the size of the two indices.

For this small dataset the difference is not that big, but with scale this has huge impact.

## Exercise 14 - Time series

In this exercise we simulate log messages and create a script that indexes a document every 5 seconds, with a timestamp and some random text.

We also create a new index every minute in the following form:

logs-YYYY-MM-DD-hh-mm

First we define the mapping of our indices. If we don't do this, Elasticsearch would map the timestamp, which is actually just a floating point number, to a float. Lets go ahead and execute the following request.

```
PUT /_template/template_logs
{
  "index_patterns": "logs-*",
  "mappings": {
    "properties": {
      "timestamp": {
        "type":   "date",
        "format": "epoch_second"
      }
    }
  }
}
```

Now we can start indexing:

```
docker-compose run --rm python python exercise-data-management/exercise-14.py
```

Wait for 5 minutes to complete the execution of the script. Once its done lets head over to Kibana.
Click on this [link](http://localhost:5601/app/kibana#/management/kibana/index_patterns) to open index patterns.

Click on create index pattern button.

Fill the index pattern input field with `logs-*`. The asterisks symbol will make sure that all indices that start with `logs-` will be included. Click next.

On the next page we are asked to tell Kibana, what is the timestamp that defines our time series. Here we will select `timestamp.` Click **Create index pattern** and head over to the [discover tab](http://localhost:5601/app/kibana#/discover). We will see our events index first. Just select `logs-*` for the select in the left top corner.

You should be able now to see the indexed documents ordered by timestamp.

## Bonus: IML to clean time series

Imagine we would never stop indexing logs and over time we add a new index every minute.

Try to define your personal index lifecycle management to cleanup old indices. The [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/index-lifecycle-management-api.html#index-lifecycle-management-api) docs are a very good place to start.

Solution can be found [here](https://github.com/aboutbits/elasticsearch-workshop/blob/master/exercise-data-management/solution-bonus.md).

