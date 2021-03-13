from ..controller.is_authed import is_authed

routes = []

routes.append(
    dict(
        rule="/is_authed", view_func=is_authed, options=dict(methods=["GET"])
    )
)
