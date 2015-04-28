from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from .forms import Form1

from bson.objectid import ObjectId
from flask.ext.login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', user=current_user)

@main.route('/form_1', methods=['GET', 'POST'])
@login_required
def form_1():
    form = Form1()
    if form.validate_on_submit():
        form_data = {
                'name': form.name.data,
                'community': form.community.data,
                'district': form.district.data,
                'title': form.title.data,
                'age': form.age.data,
                'weight': form.weight.data,
                'height': form.height.data,
                'zone': current_user.zone,
                }
        db.form1.insert(form_data, safe=True)
    return render_template('form_1.html', form=form,
            user=current_user)

@main.route('/form_1_view', methods=['GET', 'POST'])
@login_required
def form_1_view():
    return render_template('form_1_report.html', db=db)
