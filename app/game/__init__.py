# app/auth/__init__.py

from flask import Blueprint

game = Blueprint('game', __name__)

from . import views
