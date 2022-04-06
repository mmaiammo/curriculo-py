from flask import Flask
from .webapp import webapp


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    app.register_blueprint(webapp)

    return app
