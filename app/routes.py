from flask import render_template
from flask import current_app as app
from app.database_1.models import Comment_Model_1
from app.database_2.models import Comment_Model_2

@app.route("/")
@app.route("/index")
def index():
    db_1_comments = Comment_Model_1.query.all()
    db_2_comments = Comment_Model_2.query.all()

    return render_template("index.html", db_1_comments=db_1_comments, db_2_comments=db_2_comments)
