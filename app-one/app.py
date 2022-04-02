from flask import Blueprint
from flask import render_template
# from .extensions import mongo
# from flask import request
# from flask import redirect
# from flask import url_for
# from flask import session
# from flask import flash

main = Blueprint('app', __name__)


@main.route('/')
def index():
    # competencias_collection = mongo.db.competencias
    # competencias_collection.insert_one({
    #     'name': 'Modelagem em análise orientada a objetos com UML'})
    # return '<h1>Adicionado</h1>'
    return render_template('main.html')


@main.route('/novo')
def novoCurriculo():
    return render_template('curriculo.html')


@main.route('/novo', methods=["POST"])
def inserirCurriculo():
    return render_template('curriculo.html')
