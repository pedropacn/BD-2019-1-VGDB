# app/__init__.py

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
# db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    # db.init_app(app)
    Bootstrap(app)

    from app import models


    # blueprint registration
    from .dog import dog as dog_blueprint
    app.register_blueprint(dog_blueprint)

    # temporary route
    @app.route('/')
    def hello_world():
      return 'Hello, World!'

    return app
