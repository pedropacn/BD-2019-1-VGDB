# app/auth/__init__.py

from . import views
from flask import Blueprint

game = Blueprint('game', __name__)
