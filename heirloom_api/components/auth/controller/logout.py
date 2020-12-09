from flask import session

def logout():
    '''
    Logout user
    '''
    session.clear()
    return {'success': True}