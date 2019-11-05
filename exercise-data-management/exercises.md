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

Now you can navigate to the (Discover tab)[http://localhost:5601/app/kibana#/discover?_g=()].

In this view you should see all 3 documents, that have been added in the previous steps.

## Exercise 4 - Update a document

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

The document will be completely be replaced. If you skip fields, they will be removed. For example if we remove `type` from the body, it will delete the field from the document.

```
PUT /events-v1/_doc/<COPY DOCUMENT ID>
  {
    "Id": "FD7DC58E68A9447FB987460138FB3C85", 
    "Active": false,
    "Title": "100. Giro d'Italia: Start der 19. Etappe Innichen - Piancavallo" 
  }
```

Check the changes in the (Discover tab)[http://localhost:5601/app/kibana#/discover?_g=()] or with search API.

## Exercise 5 - Update a single field in a document

Lets use the single field update API to add the delete field again.

```
POST /events-v1/_doc/<COPY DOCUMENT ID>
{
    "doc" : {
        "Type": "1"
    }
}
```

Check the changes in the (Discover tab)[http://localhost:5601/app/kibana#/discover?_g=()] or with search API.
