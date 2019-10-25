Dataset
=======

The data is taken from the [Open Data Hub Südtirol - Alto Adige](https://opendatahub.bz.it). This data is Open Source and can be used by everyone.

Special thanks go to the [NOI Techpark](https://noi.bz.it) and all its [data providers](https://opendatahub.readthedocs.io/en/latest/datasets.html) for collecting and sharing the data as open data.

## Fetch

First start a Python Docker container:

```bash
docker run -it --rm -v ${PWD}:/code -w /code python bash
```

Then install the pip requirements:

```bash
pip install -r requirements.txt
```

And then last, execute the fetch command:

```bash
python3 fetch.py
```
