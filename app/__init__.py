# app/__init__.py

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# variables initialization
login_manager = LoginManager()
# db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    
    # db.init_app(app)
    Bootstrap(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app import models


    # blueprint registration

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    from .dog import dog as dog_blueprint
    app.register_blueprint(dog_blueprint)

    from .game import game as game_blueprint
    app.register_blueprint(game_blueprint)

    return app
