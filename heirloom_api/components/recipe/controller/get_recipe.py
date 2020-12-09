from bson.objectid import ObjectId
from flask import jsonify, g
from heirloom_api.db.mongo import mongo
from heirloom_api.components.auth.wrappers import login_required


@login_required
def get_recipes():
    '''
    Controller to get list of all recipes in recipe collection
    '''
    cursor = mongo.db.recipes.find()
    response = list()
    for doc in cursor:
        doc['_id'] = str(doc['_id'])
        response.append(doc)
    return jsonify(response)


@login_required
def get_recipe(recipe_id):
    '''
    controller to get individual recipe for a given recipe id
    '''
    recipe_id_object = ObjectId(recipe_id)
    response = mongo.db.recipes.find_one({'_id': recipe_id_object})
    response['_id'] = str(response['_id'])
    return jsonify(response)

@login_required
def get_recipes_by_user():
    '''
    Controller to get individual recipe for a given userid
    '''
    response = mongo.db.recipes.find_one({'created_by': g.user['id']})
    response['_id'] = str(response['_id'])
    return jsonify(response)
