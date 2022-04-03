from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/novo')
def novoCurriculo():
    return render_template('curriculo.html')


@app.route('/novo', methods=["POST"])
def inserirCurriculo():
    return render_template('curriculo.html')


if __name__ == "__main__":
    app.run(debug=True)
