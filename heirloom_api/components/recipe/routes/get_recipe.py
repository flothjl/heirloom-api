from ..controller.get_recipe import get_recipes

routes = []

routes.append(
    dict(rule="/get-recipes/", view_func=get_recipes, options=dict(methods=["GET"]))
)
