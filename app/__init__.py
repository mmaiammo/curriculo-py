from flask import Flask
# from flask import render_template
from .webapp import webapp


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    app.register_blueprint(webapp)
    # @app.route('/')
    # def index():
    #     return "Olá"

    # @app.route('/')
    # def index():
    #     return render_template('main.html')

    return app
