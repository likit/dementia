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
from ..models import LoginUser
from .. import db
from ..main.forms import Form1


# TODO: update UserForm
class UserForm(form.Form):
    # username = fields.TextField('Username',
    #         validators=[Required(), Length(1,64)])
    # email = fields.TextField('Email', validators=[Email()])
    # role = fields.TextField('Role', validators=[Required()])
    # password = fields.PasswordField('Password', validators=[Required()])
    # province = fields.TextField('Province', validators=[Required()])
    verified = fields.BooleanField(default="unchecked")


class Form1View(ModelView):
    can_create = False
    column_list = ('pid', 'firstname', 'lastname', 'district', 'age', 'province')
    column_sortable_list = ('firstname', 'lastname', 'district', 'province')

    form = Form1

    def is_accessible(self):
        return (current_user.is_authenticated() and
                current_user.role == 'admin')


class UserView(ModelView):
    column_list = ('username', 'name', 'lastname', 'role', 'position', 'phone',
           'verified', 'org', 'org_address', 'mhoo',
           'province', 'district', 'tambon', 'create_date_time')
    column_sortable_list = ('verified', 'name', 'lastname', 'role',
            'province', 'create_date_time')

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
            user = db.users.find_one({'email': form.email.data})
            if user is not None and check_password_hash(user['password'],
                    form.password.data):
                user = LoginUser(user['username'])
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') \
                        or url_for('.index'))
            else:
                flash('Admin account required.')
                form.email.data = ''
                form.password.data = ''
                return self.render('admin/login.html', form=form)
            flash('Invalid username or password')
        return self.render('admin/login.html', form=form)

class HomeView(BaseView):
    @expose('/')
    def home(self):
        return redirect(url_for('main.index'))

