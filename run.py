from flask import Flask
# from .extensions import mongo
#
from main import main

from flask_pymongo import PyMongo
mongo = PyMongo()

app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(main)
mongo.init_app(app)


# def create_app():
#     return app


# if __name__ == "__main__":
#     create_app().run()
