from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField,PasswordField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

class Login(FlaskForm):
    password = PasswordField('Password', [validators.DataRequired('Passowrd required')])
    email = StringField('Email', [validators.DataRequired('Email required')])
    submit=SubmitField("Oke")
class Konsol(FlaskForm):
    kode = StringField('code', [validators.DataRequired('Fill the code')])
    submit=SubmitField("Oke")