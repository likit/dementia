from flask import render_template, session, redirect, url_for
from datetime import datetime
from . import main
from .forms import NameForm
from .. import db

from bson.objectid import ObjectId
import flask_admin as admin
from wtforms import form, fields

from flask_admin.form import Select2Widget
from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList

from flask.ext.login import login_required, current_user

# User admin
class UserForm(form.Form):
    username = fields.TextField('Username')
    email = fields.TextField('Email')
    role = fields.TextField('Role')
    password = fields.PasswordField('Password')


class UserView(ModelView):
    column_list = ('username', 'email', 'role')
    column_sortable_list = ('username', 'email', 'password')

    form = UserForm

    def is_accessible(self):
        # return current_user.is_authenticated()
        return True

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', user=current_user)

@main.route('/user')
@login_required
def user():
    return render_template('user.html')
