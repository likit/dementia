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
    form = NameForm()
    if form.validate_on_submit():
        user = db.users.find_one({'username': form.name.data})
        session['admin'] = False
        if user is None:
            session['known'] = False
        elif user['role'] == 'admin':
            session['admin'] = True
            session['name'] = form.name.data
            return render_template('admin.html',
                    current_time=datetime.utcnow(),
                    name=session.get('name'),
                    admin=session.get('admin', False),
                    )
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('.index'))

    return render_template('index.html',
            form=form,
            )

@main.route('/user')
@login_required
def user():
    return render_template('user.html')
