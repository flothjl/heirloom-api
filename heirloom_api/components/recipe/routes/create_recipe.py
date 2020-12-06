import json

from heirloom_api.db import mongo
from ..controller.create_recipe import create_recipe

routes = []

routes.append(
    dict(
        rule="/create-recipe/", view_func=create_recipe, options=dict(methods=["POST"])
    )
)
