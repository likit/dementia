# -*- coding: utf-8 -*-

import os
import numpy as np
from flask import (render_template, session, redirect,
                        url_for, flash, jsonify, request)
from bson import json_util
from . import main
from .. import db
from .forms import Form1
from .. import APP_ROOT, APP_STATIC

from bson.objectid import ObjectId
from flask.ext.login import login_required, current_user
import json

provinces_json = json.load(open(os.path.join(APP_STATIC, 'provinces.json')))

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', user=current_user)

@main.route('/searchpid')
def searchpid():
    qpid = request.args.get('pid')
    res = db.form1.find_one({'pid': qpid})
    if res:
        return jsonify(result='found',
                firstname=res['firstname'],
                lastname=res['lastname'],
                province=res['province'],
                age=res['age'],
                district=['district'],
                amphur=['amphur'],
                )
    else:
        return jsonify(result='notfound')

@main.route('/form_1', methods=['POST', 'GET'])
@login_required
def form_1():
    form = Form1(request.form)
    form.province.choices = [('', 'Select province')] + \
            sorted([(p.get('province'), p.get('province'))
                for p in provinces_json])
    provinces = sorted([x.get('province') for x in provinces_json])

    amphurs = {}
    amphur_list = []
    for p in provinces_json:
        amphurs[p.get('province')] = p.get('amphur').keys()
        amphur_list += p.get('amphur').keys()

    districts = {}
    district_list = []
    for p in provinces_json:
        for a, t in p.get('amphur').iteritems():
            districts[a] = t
            district_list += t

    form.amphur.choices = [('', '')] + [(x,x) for x in amphur_list]
    form.district.choices = [('', '')] + [(x,x) for x in district_list]

    if form.validate_on_submit():
        form_data = {
                'firstname': form.firstname.data,
                'lastname': form.lastname.data,
                'age': form.age.data,
                # 'weight': form.weight.data,
                # 'height': form.height.data,
                'locale': current_user.province,
                'pid': form.pid.data,
                'province': form.province.data,
                'district': form.district.data,
                'amphur': form.amphur.data,
                # add "update datetime"
                # add "add datetime"
                # add "PID"
                # add "updated by"
                # add "added by"
                }
        db.form1.insert(form_data, safe=True)
        flash('Data added sucessfully.')
        return redirect(url_for('.form_1_view'))

    return render_template('form_1.html', form=form,
            user=current_user,
            districts=json_util.dumps(districts),
            provinces=json_util.dumps(provinces),
            amphurs=json_util.dumps(amphurs))

@main.route('/form_1_view', methods=['GET', 'POST'])
@login_required
def form_1_view():
    return render_template('form_1_report.html', db=db)

@main.route('/your_account')
@login_required
def your_account_view():
    user = db.users.find_one({'username': current_user.username})
    return render_template('your_account.html', db=db, user=user)

@main.route('/viz/')
@login_required
def age_viz():
    '''Visualize ages in a pie chart.'''
    males = 0
    females = 0
    others = 0
    male_ages = []
    female_ages = []
    other_ages = []
    for rec in db.form1.find():
        if rec['firstname'].encode('utf8').startswith('นาย'):
            males += 1
            male_ages.append(rec['age'])
        elif rec['firstname'].encode('utf8').startswith('นาง'):
            females += 1
            female_ages.append(rec['age'])
        elif rec['firstname'].encode('utf8').startswith('น.ส.'):
            females += 1
            female_ages.append(rec['age'])
        else:
            others += 1
            other_ages.append(rec['age'])

    piedata = [{'key': 'เพศชาย', 'y': males},
            {'key': 'เพศหญิง', 'y': females},
            {'key': 'อืนๆ', 'y': others},
            ]

    def get_boxplot_params(data):
        data = np.asarray(data)
        median = np.median(data)
        upper_quartile = np.percentile(data, 75)
        lower_quartile = np.percentile(data, 25)

        iqr = upper_quartile - lower_quartile
        upper_whisker = data[data<=upper_quartile+1.5*iqr].max()
        lower_whisker = data[data>=lower_quartile-1.5*iqr].min()
        outliers = data[data>upper_whisker]
        outliers += data[data<lower_whisker]

        values = {
                'Q1': lower_quartile,
                'Q2': median,
                'Q3': upper_quartile,
                'whisker_high': upper_whisker,
                'whisker_low': lower_whisker,
                'outliers': list(outliers),
            }
        return values

    boxplotdata = [
            {
                'label': 'เพศชาย',
                'values': get_boxplot_params(male_ages)
                },
            {
                'label': 'เพศหญิง',
                'values': get_boxplot_params(female_ages)
                },
            ]
    if other_ages:
        boxplotdata.append(
            {
                'label': 'อื่นๆ',
                'values': get_boxplot_params(other_ages)
                },
            )

    return render_template('viz/index.html', piedata=piedata,
            boxplotdata=boxplotdata)
