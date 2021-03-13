from ..controller.create_recipe import create_recipe, update_recipe

routes = []

routes.append(
    dict(
        rule="/create", view_func=create_recipe, options=dict(methods=["POST"])
    )
)

routes.append(
    dict(
        rule="/update/<recipe_id>",
         view_func=update_recipe,
         options=dict(methods=["POST"])
    )
)
