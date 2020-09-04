from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SubmitField,
    BooleanField, PasswordField)
from wtforms.validators import (ValidationError, DataRequired, Length,
    Email, EqualTo)
from app.models import User



class UserEditForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    fname = StringField('First name', validators=[DataRequired()])
    lname = StringField('Last name', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    admin = BooleanField('Is an admin')
    submit = SubmitField('Submit')

    def __init__(self, original_email, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.original_email = original_email

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=self.email.data).first()
            if user is not None:
                raise ValidationError('Email in use. Please try a different one.')

class UserDeleteForm(FlaskForm):
    submit = SubmitField('Confirm')

class UserCreateForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    fname = StringField('First name', validators=[DataRequired()])
    lname = StringField('Last name', validators=[DataRequired()])
    admin = BooleanField('Create as admin')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already registered. Please login.')
