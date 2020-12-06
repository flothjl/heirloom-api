from ....db import mongo
from ..controller.create_recipe import create_recipe
import json

routes = []

routes.append(
    dict(
        rule="/create-recipe/", view_func=create_recipe, options=dict(methods=["POST"])
    )
)
