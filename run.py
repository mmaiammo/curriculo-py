

from flask import Flask
# from .extensions import mongo
#

from main import main

from flask_pymongo import PyMongo
mongo = PyMongo()

app = Flask(__name__)


def create_app():
    app.config.from_object('settings')

    mongo.init_app(app)

    app.register_blueprint(main)

    return app


if __name__ == "__main__":
    create_app().run()
