from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

class AdminLoginForm(Form):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password',
            validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

# TODO: admin register page

# class RegistrationForm(Form):
#     email = StringField('Email', validators=[Required(),
#         Length(1,64), Email()])
#     username = StringField('Username', validators=[
#         Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#             'Usernames must have only letters, '
#             'numbers, dots or underscores')])
#     password = PasswordField('Password', validators=[
#         Required(), EqualTo('password2', message='Passwords must match.')])
#     password2 = PasswordField('Confirm password', validators=[Required()])
#     submit = SubmitField('Register')
# 
#     def validate_email(self, field):
#         if db.users.find_one({'email': field.data}):
#             raise ValidationError('Email already registered.')
# 
#     def validate_username(self, field):
#         if db.users.find_one({'username': field.data}):
#             raise ValidationError('Username already in use.')
