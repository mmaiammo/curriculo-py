from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main.html')


@main.route('/novo')
def novoCurriculo():
    return render_template('curriculo.html')


@main.route('/novo', methods=["POST"])
def inserirCurriculo():
    return render_template('curriculo.html')
