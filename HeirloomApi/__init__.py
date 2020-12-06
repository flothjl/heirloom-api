import json
import os

from flask import Flask

from db_creds import DbEnums

from .components.recipe.routes import bp as recipe_bp
from .db import mongo


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["MONGO_URI"] = DbEnums.CONNECTION_STRING
    mongo.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/testMongo")
    def test_mongo():
        return json.dumps(mongo.db.list_collection_names())

    app.register_blueprint(recipe_bp)

    return app
