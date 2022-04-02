from flask import Blueprint
from flask import render_template
# from flask import request
# from flask import redirect
# from flask import url_for
# from flask import session
# from flask import flash

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
