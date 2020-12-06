from ....db import mongo
from ....models.recipe.base_recipe import Recipe
from ..services import add_recipe
from flask import request, abort, Response, current_app
import json

def create_recipe():
    try:
        recipe = Recipe.build_from_json(request.get_json())
        object_id = add_recipe(recipe.__dict__)
        return str(object_id)
    except Exception as e:
        current_app.logger.error(f'{e}')
        abort(503)
