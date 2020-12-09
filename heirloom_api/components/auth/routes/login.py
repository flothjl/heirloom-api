from ..controller.login import login

routes = []

routes.append(
    dict(
        rule="/login", view_func=login, options=dict(methods=["POST"])
    )
)
