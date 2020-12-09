from ..controller.logout import logout

routes = []

routes.append(
    dict(
        rule="/logout", view_func=logout, options=dict(methods=["GET"])
    )
)
