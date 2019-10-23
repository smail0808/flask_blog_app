from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from flaskblog.models import User





class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # create a costum validation for username
    def validate_username(self, username):
        # check if username is in the db
        user = User.query.filter_by(username=username.data).first()
        # if user exist in db
        if user:
            raise ValidationError('username already exists. Try another?')
    # create a costum validation for email

    def validate_email(self, email):
        # check if email is in the db
        user_email = User.query.filter_by(email=email.data).first()
        # if email aleady exist in db
        if user_email:
            raise ValidationError(
                'Email already exists. you can try login with this Email?')







class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login Up')






class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # create a costum validation for username
    def validate_username(self, username):
        if username.data != current_user.username:
            # check if username is in the db
            user = User.query.filter_by(username=username.data).first()
            # if user exist in db
            if user:
                raise ValidationError('username already exists. Try another?')
    # create a costum validation for email

    def validate_email(self, email):
        if email.data != current_user.email:
            # check if email is in the db
            user_email = User.query.filter_by(email=email.data).first()
            # if email exist in db
            if user_email:
                raise ValidationError('Email already exists. Try another?')







class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        # check if email is in the db
        user = User.query.filter_by(email=email.data).first()
        # if email don't exist in db
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first!')







class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
                             DataRequired(), length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')