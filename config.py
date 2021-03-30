import os

#set absolute path to base directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # configure database route to basedir
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
