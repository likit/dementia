from flask_admin.form import Select2Widget
from flask_admin.contrib.pymongo import ModelView, filters
from flask_admin.model.fields import InlineFormField, InlineFieldList
from flask_admin import AdminIndexView, expose, BaseView
from wtforms import form, fields
from wtforms.validators import Email, Length, Required
from flask.ext.login import current_user, login_user
from flask import redirect, url_for, render_template, flash, request
from werkzeug.security import check_password_hash
from datetime import datetime
from .forms import AdminLoginForm
from ..models import User
from .. import db
from ..main.forms import Form1


class UserForm(form.Form):
    username = fields.TextField('Username',
            validators=[Required(), Length(1,64)])
    email = fields.TextField('Email', validators=[Email()])
    role = fields.TextField('Role', validators=[Required()])
    # password = fields.PasswordField('Password', validators=[Required()])
    zone = fields.TextField('Zone', validators=[Required()])


class Form1View(ModelView):
    can_create = False
    column_list = ('title', 'name', 'district', 'age', 'zone')
    column_sortable_list = ('name', 'district', 'zone')

    form = Form1

    def is_accessible(self):
        return (current_user.is_authenticated() and
                current_user.role == 'admin')


class UserView(ModelView):
    column_list = ('username', 'name', 'lastname', 'email', 'role',
           'verified', 'zone', 'create_date_time')
    column_sortable_list = ('verified', 'name', 'lastname', 'role',
            'zone', 'create_date_time')

    form = UserForm

    def is_accessible(self):
        return (current_user.is_authenticated() and
                current_user.role == 'admin')

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('.login_view'))


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if (not current_user.is_authenticated() or
                current_user.role != 'admin'):
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=['GET', 'POST'])
    def login_view(self):
        form = AdminLoginForm()
        if form.validate_on_submit():
            user = db.users.find_one({'username': form.username.data})
            if user is not None and check_password_hash(user['password'],
                    form.password.data):
                if user['role']=='admin':
                    #FIXME: use email instead?
                    user = User(user['username'], user['zone'], user['role'])
                    login_user(user, form.remember_me.data)
                    return redirect(request.args.get('next') \
                            or url_for('.index'))
                else:
                    flash('Admin account required.')
                    form.username.data = ''
                    form.password.data = ''
                    return render_template('admin/login.html',
                            form=form)
            flash('Invalid username or password')
        return self.render('admin/login.html', form=form)

class HomeView(BaseView):
    @expose('/')
    def home(self):
        return redirect(url_for('main.index'))

