from flask import request, session
from werkzeug.security import check_password_hash

from heirloom_api.db.auth import get_db

from ..services import AuthDb

def login():
    '''
    logs a user in and adds a session entry if password matches
    '''
    payload = request.get_json()
    username = payload['username']
    password = payload['password']
    database = AuthDb(get_db())
    error = None
    user = database.login(username)
    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return {'success': True, 'msg': 'success', 'data':session.get('user_id')}

    return {'success': False, 'msg': error}
