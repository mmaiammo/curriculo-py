from flask import Flask
from databases import dbmongo

from routes.main import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(".settings.py")
    app.register_blueprint(main)

    # config_object = "settings"
    dbmongo.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run()
