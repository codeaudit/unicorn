from elasticsearch import Elasticsearch

import sys
import os

# default configuration settings (localhost:9200)
es = Elasticsearch()
q = { "type": "fs",
        "settings": {
            "location": "/big/backups/",
            "compress": True
            }
        }

es.snapshot.create_repository(repository='unicorn_backups', body=q)
