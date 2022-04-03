from flask import Blueprint
from flask import render_template
# from flask import Flask
# from flask import request
# from flask import url_for
# from flask import redirect
# from flask import flash
# from flask import render_template

webapp = Blueprint('webapp', __name__)


@webapp.route('/')
def index():
    return render_template('main.html')


# @run.route('/novo')
# def novoCurriculo():
#     return render_template('curriculo.html')


# @run.route('/novo', methods=["POST"])
# def inserirCurriculo():
#     return render_template('curriculo.html')
