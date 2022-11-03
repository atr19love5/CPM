from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField

from wtforms import validators


class Login(FlaskForm):
    password = PasswordField(
        'Password', [validators.DataRequired('Passowrd required')])
    email = StringField('Email', [validators.DataRequired('Email required')])
    submit = SubmitField("Oke")


class Cdata(FlaskForm):
    cname = StringField('Name')
    cnamer = BooleanField('Rainbow Name')
    cmoney = IntegerField('Money')
    ccoin = IntegerField('Coin')
    chorn = BooleanField('Unlock Horn')
    csirine = BooleanField('Unlock Sirine')
    submit = SubmitField("Oke")
