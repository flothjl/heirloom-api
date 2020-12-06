routes = []

def hello_world():
    return 'hello from recipes'

routes.append(dict(
    rule='/hello-world/',
    view_func=hello_world,
    options=dict(methods=['GET'])))