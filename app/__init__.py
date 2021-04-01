from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# import blueprints and bp level SQLAlchemy intances
from .database_2 import database_2
from app.database_2.models import db as db_2

# create an instance of migrate not bound to app outside of app context
migrate = Migrate()

def create_app():
    # create an instance of Flask object and configure from object
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # initialize db and migration instances within the app
    db_2.init_app(app)
    migrate.init_app(app, db_2)

    with app.app_context():
        # create databases within app context
        db_2.create_all()
        
        # register bluprints within app context
        app.register_blueprint(database_2, url_prefix="/database_2")

        # import app level routes at end to avoid circular imports
        from app import routes

        return app