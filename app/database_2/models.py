from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Database_2_DB(db.Model):
    id = db.Column(db.Integer, primary_key=True) # <-- NB. Autoincrement defaults to true on primary int key cols (SQLAlchemy)
    comment = db.Column(db.String(144), index=True)
   