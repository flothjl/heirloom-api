import json

from heirloom_api.db import mongo


def get_recipes():
    '''
    Controller to get list of all recipes in recipe collection
    '''
    return json.dumps(mongo.db.recipes.find())
