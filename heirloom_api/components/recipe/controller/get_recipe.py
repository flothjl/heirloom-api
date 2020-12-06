import json

from heirloom_api.db import mongo


def get_recipes():
    return json.dumps([recipe for recipe in mongo.db.recipes.find()])
