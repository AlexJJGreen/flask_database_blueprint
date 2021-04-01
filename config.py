import os

#set absolute path to base directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # set secret key to use wtf-forms -- prevents CSRF attacks
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a secret string key"
    # configure database route to basedir
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
