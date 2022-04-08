import requests
# type: ignore
# import json

from flask import Blueprint
from flask import render_template

webapp = Blueprint('webapp', __name__)


@webapp.route('/')
def index():
    return render_template('curriculo/curriculo.html')


@webapp.route('/list')
def list():
    response = requests.get(
        "https://curriculo-node.herokuapp.com/curriculos")
    curriculos = response.json()
    return render_template('curriculo/list.html', curriculos=curriculos)
