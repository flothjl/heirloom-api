from ...db import mongo
from flask import make_response
def add_recipe(value: dict):
    response = mongo.db.recipes.insert_one(value)
    object_id = response.inserted_id
    if object_id:
        return object_id