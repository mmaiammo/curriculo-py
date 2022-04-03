from flask import Flask

from main import main

from flask_pymongo import PyMongo
mongo = PyMongo()

app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(main)
