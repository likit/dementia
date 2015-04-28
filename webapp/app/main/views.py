from flask import render_template, session, redirect, url_for
from . import main
from .. import db

from bson.objectid import ObjectId
from flask.ext.login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', user=current_user)

@main.route('/user')
@login_required
def user():
    return render_template('user.html')
