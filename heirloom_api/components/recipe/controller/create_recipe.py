from time import time
from flask import abort, current_app, request, g
from heirloom_api.models.exceptions import InvalidRequestBody
from heirloom_api.models.recipe.base_recipe import Recipe
from heirloom_api.components.auth.wrappers import login_required
from ..services import add_recipe, update_recipe as db_update_recipe


@login_required
def create_recipe():
    '''
    Returns: db objectID
    '''
    try:
        print(f'{request.get_json()}')
        recipe = Recipe.build_from_json(request.get_json())
        
        recipe = {'created_by': g.user['id'],
                  'created': int(time()),
                  **recipe.__dict__}
        object_id = add_recipe(recipe)
        return str(object_id)
    except InvalidRequestBody as error:
        current_app.logger.error(f"{error}")
        abort(400)

@login_required
def update_recipe(recipe_id):
    '''
    Returns: db objectID
    '''
    try:
        recipe = Recipe.build_from_json(request.get_json())
        recipe = {'created_by': g.user['id'],
                  'created': int(time()),
                  **recipe.__dict__}
        db_update_recipe(recipe, recipe_id)
        return 'success'
    except InvalidRequestBody as error:
        current_app.logger.error(f"{error}")
        abort(400)
