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
