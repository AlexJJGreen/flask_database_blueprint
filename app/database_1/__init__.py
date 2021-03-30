from flask import Blueprint

database_1 = Blueprint("database_1", __name__, static_folder="/static", template_folder="templates")

from . import models, routes, forms