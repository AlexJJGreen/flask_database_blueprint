from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Database_2_Form(FlaskForm):
    comment = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")