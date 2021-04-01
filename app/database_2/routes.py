from flask import render_template, redirect, url_for
from . import database_2
from .forms import Comment_Form
from .models import Comment_Model, db

@database_2.route("db_2_form", methods=["GET", "POST"])
def db_2_form():
    form = Comment_Form()
    if form.validate_on_submit():
        comment = Comment_Model(comment=form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("form.html", form=form)

        
