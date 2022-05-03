from lib2to3.pgen2 import token
import requests
# type: ignore
# import json
from flask import current_app
from flask import Blueprint
from flask import render_template

webapp = Blueprint('webapp', __name__)


@webapp.route('/')
def index():
    return render_template('curriculo/curriculo.html')


@webapp.route('/list')
def list():
    url = current_app.config["API_MONGO"] + "api/curriculo/findAll"
    response = requests.get(url)
    curriculos = response.json()
    return render_template('curriculo/list.html',
                           curriculos=curriculos["curriculo"])


@webapp.route('/list/<id>')
def listone(id):
    url = current_app.config["API_MONGO"] + '/' + id
    response = requests.get(url)
    curriculos = response.json()
    return render_template('curriculo/list.html', curriculos=curriculos)


@webapp.route('/novo')
def create():
    response = requests.post(
        "https://curriculo-node.herokuapp.com/curriculos")
    curriculos = response.json()
    return render_template('curriculo/list.html', curriculos=curriculos)


@webapp.route('/edit/<string:id>')
def edit(id):
    data_login = {
        "username": "day",
        "password": "jean2004"
    }
    url = "https://curriculo-node.herokuapp.com/api/auth/signin"

    response = requests.post(url=url, json=data_login)

    data_res = response.json()
    token = data_res['accessToken']
    return render_template('curriculo/edit.html')


@webapp.route('/sobre')
def about():
    return render_template('help/about.html')
