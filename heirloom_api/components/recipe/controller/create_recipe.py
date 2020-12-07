from flask import abort, current_app, request
from heirloom_api.models.exceptions import InvalidRequestBody
from heirloom_api.models.recipe.base_recipe import Recipe
from ..services import add_recipe


def create_recipe():
    '''
    Returns: db objectID
    '''
    try:
        recipe = Recipe.build_from_json(request.get_json())
        object_id = add_recipe(recipe.__dict__)
        return str(object_id)
    except InvalidRequestBody as error:
        current_app.logger.error(f"{error}")
        abort(400)
