import os
from flask import Flask


def create_app(test_config=None):
    # This is for creating and configuring the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="Dennis",
        DATABASE=os.path.join(app.instance_path, '')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Ensuring the instance folder exists in the project
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Create an index page
    @app.route("/")
    def index():
        return "Hello world. I will concur you"

    return app
