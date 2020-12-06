from .get_recipe import routes as get_recipe
from .create_recipe import routes as create_recipe 
from .hello_world import routes as test_routes

import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('recipes', __name__, url_prefix='/recipes')
routes = (get_recipe + test_routes + create_recipe)

for r in routes:
    bp.add_url_rule(
        r['rule'],
        endpoint=r.get('endpoint', None),
        view_func=r['view_func'],
        **r.get('options', {}))
