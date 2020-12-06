from flask import request, abort, Response, current_app
import json

from ....db import mongo
from ....models.recipe.base_recipe import Recipe
from ....models.exceptions import InvalidRequestBody
from ..services import add_recipe


def create_recipe():
    try:
        recipe = Recipe.build_from_json(request.get_json())
        object_id = add_recipe(recipe.__dict__)
        return str(object_id)
    except InvalidRequestBody as e:
        current_app.logger.error(f"{e}")
        abort(400)
