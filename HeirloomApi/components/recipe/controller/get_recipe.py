import json

from HeirloomApi.db import mongo


def get_recipes():
    return json.dumps([recipe for recipe in mongo.db.recipes.find()])
