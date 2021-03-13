from heirloom_api.components.auth.wrappers import login_required

@login_required
def is_authed():
    '''
    check to see if a user is logged in
    '''
    return {'success': True}