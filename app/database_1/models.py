from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comment_Model_1(db.Model):
    id = db.Column(db.Integer, primary_key=True) # <-- NB. Autoincrement defaults to true on primary int key cols (SQLAlchemy)
    comment = db.Column(db.String(144), index=True)

    def __init__(self, comment):
        self.comment = comment
   