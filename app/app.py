from flask import Flask
from databases import dbmongo

from .routes.main import main


def create_app(config_object="app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(main)

    dbmongo.init_app(app)
    return app
