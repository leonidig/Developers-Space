from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField, 
    EmailField, 
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email
)


class LoginForm(FlaskForm):
    nickname = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(),])
    
    submit = SubmitField("Log In")