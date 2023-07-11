from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskrental.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please Enter a name'), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(message='Please Enter an email'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Please Enter a password')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message='Passwords do not match'), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            self.username.errors += (ValidationError("That username is taken. Please Choose a different username"),)

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            self.email.errors += (ValidationError("That email is already registered. Please Login or forget password"),)
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Please Enter an email'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Please Enter a password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please Enter a name'), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(message='Please Enter an email'), Email()])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                self.username.errors += (ValidationError("That username is taken. Please Choose a different username"),)

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                self.email.errors += (ValidationError("That email is already registered. Please Login or forget password"),)

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Please Enter an email'), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            self.email.errors += (ValidationError("If there is an account with this email an email will be sent"))

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(message='Please Enter a password')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message='Passwords do not match'), EqualTo('password')])
    submit = SubmitField('Reset Password')