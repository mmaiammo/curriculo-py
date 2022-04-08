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
        "https://curriculo-node.herokuapp.com/competencias")
    competencias = response.json()
    print('req:', competencias)
    return render_template('curriculo/list.html', competencias=competencias)
