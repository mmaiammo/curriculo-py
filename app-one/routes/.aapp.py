from flask import Flask
# from databases import mongo
from routes.main import main

app = Flask(__name__)

# mongo.init_app(app)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)