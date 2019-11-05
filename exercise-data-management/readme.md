# Data Management

## Set up

Start the containers by executing the following command inside the current directory:

```bash
docker-compose up --build --detach
```

You can access Kibana (Web UI) using this URL: [http://localhost:5601/](http://localhost:5601/).

Most of the exercises can be done directly using Kibana.

## Download the dataset

```bash
docker-compose run --rm python python dataset/fetch.py
```

## Tear down

Stop the containers by executing the following command inside the current directory:

```bash
docker-compose down
```
