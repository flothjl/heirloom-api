import json

from flask import Response, abort, current_app, request

from HeirloomApi.db import mongo
from HeirloomApi.models.exceptions import InvalidRequestBody
from HeirloomApi.models.recipe.base_recipe import Recipe
from ..services import add_recipe


def create_recipe():
    try:
        recipe = Recipe.build_from_json(request.get_json())
        object_id = add_recipe(recipe.__dict__)
        return str(object_id)
    except InvalidRequestBody as e:
        current_app.logger.error(f"{e}")
        abort(400)
