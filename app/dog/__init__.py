# app/auth/__init__.py

from flask import Blueprint

dog = Blueprint('dog', __name__)

from . import views