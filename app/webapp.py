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
    response = requests.get(current_app.config["API_MONGO"])
    curriculos = response.json()
    return render_template('curriculo/list.html', curriculos=curriculos)


# router.get('/:id', UserController.findOne)


@webapp.route('/list/<id>')
def listone(id):
    # , "?/:62502f5a559389bd6aaa7fbc"
    url = current_app.config["API_MONGO"] + '/' + id
    # print(url)

    response = requests.get(url)
    curriculos = response.json()
    # print(curriculos)
    return render_template('curriculo/list.html', curriculos=curriculos)


@webapp.route('/novo')
def create():
    response = requests.post(
        "https://curriculo-node.herokuapp.com/curriculos")
    curriculos = response.json()
    # print(curriculos)
    return render_template('curriculo/list.html', curriculos=curriculos)


@webapp.route('/editar')
def edit():
    response = requests.get(
        "https://curriculo-node.herokuapp.com/curriculos")
    curriculos = response.json()
    return render_template('curriculo/list.html', curriculos=curriculos)
