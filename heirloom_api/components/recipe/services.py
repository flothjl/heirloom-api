from bson import ObjectId
from heirloom_api.db.mongo import mongo


def add_recipe(value: dict):
    '''
    db service to insert document into recipes collection
    '''
    response = mongo.db.recipes.insert_one(value)
    object_id = response.inserted_id
    if object_id:
        return object_id
    return None

def update_recipe(value: dict, object_id):
    '''
    db service to update document in recipe collection
    '''
    response = mongo.db.recipes.update_one({'_id': ObjectId(object_id)}, {'$set': value})
    return response
