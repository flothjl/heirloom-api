from flask import (
    Blueprint
)

from .create_recipe import routes as create_recipe
from .get_recipe import routes as get_recipe
from .hello_world import routes as test_routes

bp = Blueprint("recipes", __name__, url_prefix="/recipes")
routes = get_recipe + test_routes + create_recipe

for r in routes:
    bp.add_url_rule(
        r["rule"],
        endpoint=r.get("endpoint", None),
        view_func=r["view_func"],
        **r.get("options", {})
    )
