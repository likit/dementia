from flask import render_template, redirect, request, flash, url_for
from . import auth
from .. import db
from datetime import datetime
from flask.ext.login import login_user, login_required, logout_user
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.users.find_one({'username': form.username.data})
        if user is not None:
            #FIXME: use email instead?
            user = User(user['username'])
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') \
                    or url_for('main.index'))
        flash('Invalid username')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('main.index'))
