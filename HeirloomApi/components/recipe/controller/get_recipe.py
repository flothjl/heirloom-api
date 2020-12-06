import json

from ....db import mongo

def get_recipes():
    return json.dumps(mongo.db.list_collection_names())