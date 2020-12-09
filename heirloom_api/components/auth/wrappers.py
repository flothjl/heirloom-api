import functools
from flask import g, abort

def login_required(view):
    '''
    wrapper for authenticated routes
    '''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(401)

        return view(**kwargs)

    return wrapped_view
