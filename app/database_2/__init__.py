from flask import Blueprint

database_2 = Blueprint("database_2", __name__, static_folder="/static", template_folder="templates")

from . import models, routes, forms