from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

from wtforms import validators

class Login(FlaskForm):
    password = PasswordField('Password', [validators.DataRequired('Passowrd required')])
    email = StringField('Email', [validators.DataRequired('Email required')])
    submit=SubmitField("Oke")
class Konsol(FlaskForm):
    cname = StringField('Change Name')
    submit=SubmitField("Oke")