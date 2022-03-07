from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from flask_wtf import FlaskForm
from ..models import User


class RegistrationForm(FlaskForm):
    """
    RegstrationForm class that passes in the required details for validation
    """

    email = StringField('your email address', validators=[Required(), Email()])
    username = StringField('your username', validators=[Required()])
    password = PasswordField('password', validators=[Required(), EqualTo('password',message=' your passwords must match')])
    password_confirm = PasswordField('confirm password', validators=[Required()])
    submit = SubmitField('sign Up')


    #custom validators
    def validate_email(self, data_field):
        """
        Functions takes in the data field and checks  database to confirm user's Validation
        """
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account already using that email')


    def validate_username(self, data_field):
        """
        Function checks if the username is unique and raises ValidationError
        """
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That user name is already used. please input another name!')


