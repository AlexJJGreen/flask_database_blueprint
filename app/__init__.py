from flask import Flask
from config import Config
from flask_migrate import Migrate

# create an instance of migrate not bound to app outside of app context
migrate = Migrate()

def create_app():
    # create an instance of Flask object and configure from object
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # import blueprints within app context
    with app.app_context():
        # import the blueprint
        from database_1 import database_1
        # import the SQLAlchemy instance
        from database_1.models import db as database_1_db
        # register the blueprint
        app.register_blueprint(database_1, url_prefix="/database_1")

        # repeat for all blueprints and databases
        from database_2 import database_2
        from database_2.models import db as database_2_db
        app.register_blueprint(database_2, url_prefix="/database_2")

        # intialize the databases passing app as arg
        database_1_db.init_app(app)
        database_2_db.init_app(app)

        # initialize the database migrations for each db instance
        migrate.init_app(app, database_1_db)
        migrate.init_app(app, database_2_db)

        # create databases
        database_1_db.create_all()
        database_2_db.create_all()

        # import routes at end to avoid circular imports
        from app import routes

        return app