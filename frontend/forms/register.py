from quart_wtf import QuartForm
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo)
from wtforms.widgets import PasswordInput


class RegisterForm(QuartForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please enter your password'),
            EqualTo('password_confirm', message='Passwords must match'),
            
        ]
    )

