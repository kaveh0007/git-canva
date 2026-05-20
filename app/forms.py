from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class UsernameForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    fetch = SubmitField("Fetch")
