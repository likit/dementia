from flask import render_template, redirect, request, flash, url_for
from . import auth
from .. import db
from datetime import datetime
from flask.ext.login import login_user, login_required, logout_user
from .forms import LoginForm, RegistrationForm
from ..models import User
from werkzeug.security import check_password_hash, generate_password_hash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.users.find_one({'username': form.username.data})
        if user is not None and check_password_hash(user['password'],
                form.password.data):
            #FIXME: use email instead?
            user = User(user['username'])
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') \
                    or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_doc = {
                'username': form.username.data,
                'email': form.email.data,
                'password': generate_password_hash(form.password.data)}
        db.users.insert(user_doc, safe=True)

        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
