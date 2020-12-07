routes = []


def hello_world():
    '''
    basic controller for the hello-world route
    '''
    return "hello from recipes"


routes.append(
    dict(rule="/hello-world/", view_func=hello_world, options=dict(methods=["GET"]))
)
