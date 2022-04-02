from flask import Flask
# from databases import dbmongo

from routes.main import main


def create_app(config_object="config"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(main)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
