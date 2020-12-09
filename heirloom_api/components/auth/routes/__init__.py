from flask import (
    Blueprint, session, g
)

from heirloom_api.db.auth import get_db

from .login import routes as login_routes
from .logout import routes as logout_routes
from .register import routes as register_routes

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.before_app_request
def load_logged_in_user():
    '''
    sets g.user attribute if user is authenticated
    '''
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

routes = login_routes + register_routes + logout_routes

for r in routes:
    bp.add_url_rule(
        r["rule"],
        endpoint=r.get("endpoint", None),
        view_func=r["view_func"],
        **r.get("options", {})
    )
