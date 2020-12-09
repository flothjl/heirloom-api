from ..controller.register import register

routes = []

routes.append(
    dict(
        rule="/register", view_func=register, options=dict(methods=["POST"])
    )
)
