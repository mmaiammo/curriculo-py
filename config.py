"""Flask configuration."""
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    API_MONGO = "https://curriculo-node.herokuapp.com/"


class ProductionConfig(Config):
    DEBUG = False
    API_MONGO = "https://curriculo-node.herokuapp.com/"


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    API_MONGO = "https://curriculo-node.herokuapp.com/"

    # API_MONGO = "http://127.0.0.1:3000/curriculo"
