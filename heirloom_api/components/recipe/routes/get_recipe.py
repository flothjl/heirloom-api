from ..controller.get_recipe import get_recipes, get_recipe, get_recipes_by_user

routes = []

routes.append(
    dict(rule="/get-recipes/",
         view_func=get_recipes,
         options=dict(methods=["GET"]))
)

routes.append(
    dict(rule="/get-recipe/<recipe_id>",
         view_func=get_recipe,
         options=dict(methods=["GET"]))
)

routes.append(
    dict(rule="/get-user-recipes/",
         view_func=get_recipes_by_user,
         options=dict(methods=["GET"]))
)
