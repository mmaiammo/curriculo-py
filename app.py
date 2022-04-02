from flask import Flask
from databases import mongo
from routes.main import main

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
mongo.init_app(app)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
