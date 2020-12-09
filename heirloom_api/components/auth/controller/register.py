from flask import request

from heirloom_api.db.auth import get_db
from ..services import AuthDb

def register():
    '''
    function to register a new user
    '''
    payload = request.get_json()
    username = payload['username']
    password = payload['password']
    database = AuthDb(get_db())
    error = None
    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif database.get_user_by_username(username).fetchone() is not None:
        error = 'User {} is already registered.'.format(username)

    if error is None:
        db_response = database.add_user(username, password)
        return db_response
    return dict(success=False, msg=error)
