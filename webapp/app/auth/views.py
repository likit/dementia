# -*- coding: UTF-8 -*-
import copy

from collections import defaultdict
from bson import json_util
from flask import request

from flask import (render_template, redirect, request,
                        flash, url_for, current_app)
from . import auth
from .. import db
from datetime import datetime
from flask.ext.login import login_user, login_required, logout_user
from .forms import LoginForm, RegistrationForm
from ..models import User
from ..email import send_email
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.users.find_one({'username': form.pid.data})
        if user is not None and check_password_hash(user['password'],
                form.password.data):
            #FIXME: use email instead?
            user = User(user['username'], user['province'], user['role'])
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
    form = RegistrationForm(request.form)
    form.province.choices = [('', 'Select province')] + \
            sorted([(x.get('province'), x.get('province'))
            for x in db.provinces.find()], key=lambda x: x[0])
    provinces = sorted([x.get('province')
            for x in db.provinces.find()], key=lambda x: x[0])

    amphurs = {}
    amphur_list = []
    for prov in db.provinces.find():
        amphurs[prov.get('province')] = prov.get('amphur').keys()
        amphur_list += prov.get('amphur').keys()

    tambons = {}
    tambon_list = []
    for prov in db.provinces.find():
        for a, t in prov.get('amphur').iteritems():
            tambons[a] = t
            tambon_list += t

    form.district.choices = [('', '')] + [(x,x) for x in amphur_list]
    form.tambon.choices = [('', '')] + [(x,x) for x in tambon_list]

    if form.validate_on_submit():
        user_doc = {
                'username': form.pid.data, # pid is used as a username
                'password': generate_password_hash(form.password.data),
                'title': form.title.data,
                'name': form.name.data,
                'lastname': form.lastname.data,
                'position': form.position.data,

                # TODO: use telephone field
                'phone': form.phone.data,
                'cell': form.cell.data,

                'org': form.org.data,
                'org_address': form.org_address.data,
                'mhoo': form.mhoo.data,
                'province': form.province.data,
                'district': form.district.data,
                'tambon': form.tambon.data,
                'objective': form.objective.data,
                'verified': False,
                'create_date_time': datetime.today(),
                'role': 'staff',
                }

        db.users.insert(user_doc, safe=True)
        send_email(to=current_app.config['ADMIN_EMAIL'],
                subject=u' New Account verification: ชื่อผู้ขอใช้ %s %s' % \
                        (form.name.data, form.lastname.data),
                template='auth/email/confirm', user=user_doc)

        flash(u'ระบบได้ส่งข้อมูลของท่านไปรอการตรวจสอบจากเจ้าหน้าที่แล้ว\n'
                u'ท่านสามารถทำการลงชื่อเข้าใช้เพื่อตรวจสอบสถานะได้ตลอดเวลา')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form,
                                provinces=json_util.dumps(provinces),
                                amphurs=json_util.dumps(amphurs),
                                tambons=json_util.dumps(tambons))


# @auth.route('/confirm')
# @login_required
# def resend_confirmation():
#         token = user.generate_confirmation_token()
#         send_email(user.email, 'Confirm Your Account',
#                 'auth/email/confirm', user=user, token=token)
#         flash('A confirmation has been sent to your email.')
#         return redirect(url_for('main.index'))
