from flask_admin.form import Select2Widget
from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList
from flask_admin import AdminIndexView, expose
from wtforms import form, fields
from flask.ext.login import current_user
from flask import redirect, url_for, render_template, flash
from datetime import datetime
from .forms import AdminLoginForm
from .models import User
from . import db


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
        return current_user.is_authenticated()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('.login_view'))


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=['GET', 'POST'])
    def login_view(self):
        form = AdminLoginForm()
        if form.validate_on_submit():
            user = db.users.find_one({'username': form.username.data})
            if user is not None and check_password_hash(user['password'],
                    form.password.data and user['role']=='admin'):
                #FIXME: use email instead?
                user = User(user['username'])
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') \
                        or url_for('.index'))
        flash('Invalid username or password')
        return render_template('admin/login.html', form=form)
