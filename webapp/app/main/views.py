from flask import render_template, session, redirect, url_for
from datetime import datetime
from . import main
from .forms import NameForm
from .. import mongo
# from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    pass
    form = NameForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({'username': form.name.data})
        session['admin'] = False
        if user is None:
            # user = User(username=form.name.data)
            # db.session.add(user)
            session['known'] = False
        elif user['role'] == 'admin':
            session['admin'] = True
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))

    return render_template('index.html',
            current_time=datetime.utcnow(),
            name=session.get('name'),
            form=form,
            known=session.get('known', False),
            admin=session.get('admin', False),
            )

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

