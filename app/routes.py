from flask import render_template
from flask import current_app as app
from app.database_2.models import Comment_Model

@app.route("/")
@app.route("/index")
def index():
    db_2_comments = Comment_Model.query.all()

    return render_template("index.html", db_2_comments=db_2_comments)
