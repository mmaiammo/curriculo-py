from flask import Flask
#from databases import dbmongo

from routes.main import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
