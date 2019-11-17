import json
from elasticsearch import Elasticsearch

def import_dataset(name, file_name, index_name, properties = {}):
    es = Elasticsearch(["elasticsearch"])

    es.indices.delete(index=index_name, ignore_unavailable=True)
    es.indices.create(index=index_name, body={
        'mappings': {
            'properties': properties
        }
    })

    with open(file_name) as file:
        items = json.load(file)

        for item in items:
            es.index(index=index_name, id=item['Id'], body=item)

        print('{0}: {1} items imported'.format(name, len(items))) 


properties_accommodations = {
    'AccoTypeId': {
        'type': 'keyword'
    },
    'AccoCategoryId': {
        'type': 'keyword'
    },
    'Features': {
        'properties': {
            'Name': {
                'type': 'keyword'
            }
        }
    },
    'LocationInfo': {
        'properties': {
            'RegionInfo': {
                'properties': {
                    'Name': {
                        'properties': {
                            'en': {
                                'type': 'text'
                            },
                            'de': {
                                'type': 'text'
                            },
                            'it': {
                                'type': 'text'
                            }
                        }
                    }
                }
            },
            'DistrictInfo': {
                'properties': {
                    'Name': {
                        'properties': {
                            'en': {
                                'type': 'text'
                            },
                            'de': {
                                'type': 'text'
                            },
                            'it': {
                                'type': 'text'
                            }
                        }
                    }
                }
            },
            'MunicipalityInfo': {
                'properties': {
                    'Name': {
                        'properties': {
                            'en': {
                                'type': 'text'
                            },
                            'de': {
                                'type': 'text'
                            },
                            'it': {
                                'type': 'text'
                            }
                        }
                    }
                }
            }
        }
    }
}

properties_activities = {
    'Difficulty': {
        'type': 'integer'
    }
}

properties_articles = {
    'Type': {
        'type': 'keyword'
    },
    'ArticleDate': {
        'type': 'date',
        'format': 'date_hour_minute_second'
    },
    'HasLanguage': {
        'type': 'keyword'
    },
    'Active': {
        'type': 'boolean'
    },
    'Detail': {
        'properties': {
            'en': {
                'properties': {
                    'Title': {
                        'type': 'text',
                        'analyzer': 'english'
                    },
                    'Header': {
                        'type': 'text',
                        'analyzer': 'english'
                    },
                    'SubHeader': {
                        'type': 'text',
                        'analyzer': 'english'
                    },
                    'IntroText': {
                        'type': 'text',
                        'analyzer': 'english'
                    },
                    'BaseText': {
                        'type': 'text',
                        'analyzer': 'english'
                    }
                }
            },
            'de': {
                'properties': {
                    'Title': {
                        'type': 'text',
                        'analyzer': 'german'
                    },
                    'Header': {
                        'type': 'text',
                        'analyzer': 'german'
                    },
                    'SubHeader': {
                        'type': 'text',
                        'analyzer': 'german'
                    },
                    'IntroText': {
                        'type': 'text',
                        'analyzer': 'german'
                    },
                    'BaseText': {
                        'type': 'text',
                        'analyzer': 'german'
                    }
                }
            },
            'it': {
                'properties': {
                    'Title': {
                        'type': 'text',
                        'analyzer': 'italian'
                    },
                    'Header': {
                        'type': 'text',
                        'analyzer': 'italian'
                    },
                    'SubHeader': {
                        'type': 'text',
                        'analyzer': 'italian'
                    },
                    'IntroText': {
                        'type': 'text',
                        'analyzer': 'italian'
                    },
                    'BaseText': {
                        'type': 'text',
                        'analyzer': 'italian'
                    }
                }
            }
        }
    }
}

import_dataset('Accommodations', 'dataset/accommodations.json', 'accommodations', properties_accommodations)
import_dataset('Activities', 'dataset/activities.json', 'activities', properties_activities)
import_dataset('Articles', 'dataset/articles.json', 'articles', properties_articles)
