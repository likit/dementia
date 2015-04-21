from flask import render_template, redirect, session
from . import auth
from ..main.forms import NameForm
from .. import db
from datetime import datetime

@auth.route('/login', methods=['GET', 'POST'])
def login():
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

    return render_template('/auth/login.html', form=form)
