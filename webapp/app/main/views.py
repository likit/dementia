# -*- coding: utf-8 -*-

import os
from datetime import datetime

import numpy as np
import json

from flask import (render_template, session, redirect,
                        url_for, flash, jsonify, request)
from bson import json_util
from . import main
from .. import db
from .forms import Form1
from .. import APP_ROOT, APP_STATIC

from bson.objectid import ObjectId
from flask.ext.login import login_required, current_user


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
    provinces_json = json.load(open(os.path.join(APP_STATIC, 'provinces.json')))
    amphurs_json = json.load(open(os.path.join(APP_STATIC, 'amphurs.json')))

    form.province.choices = [('', 'Select province')] + \
            [(p, p) for p in sorted(provinces_json)]

    districts_list = []
    for t in amphurs_json.itervalues():
        districts_list += t

    form.amphur.choices = [('', '')] + [(x,x) for x in amphurs_json.keys()]
    form.district.choices = [('', '')] + [(x,x) for x in districts_list]

    if form.validate_on_submit():
    	insert_datetime = datetime.utcnow()
        form_data = {
                'firstname': form.firstname.data,
                'lastname': form.lastname.data,
                'pid': form.pid.data,
                'street_number': form.street_number.data,
                'district_number': form.district_number.data,
                'province': form.province.data,
                'amphur': form.amphur.data,
                'district': form.district.data,
                'age': form.age.data,
                'gender': form.gender.data,
                'marital': form.marital.data,
                'marital_other': form.marital_other.data,
                'edu': form.edu.data,
                'edu_other': form.edu_other.data,
                'edu_years': form.edu_years.data,
                'living': form.living.data,
                'living_caregiver': form.living_caregiver.data,
                'living_other': form.living_other.data,
                'income': form.income.data,
                'elder_club': form.elder_club.data,
                'health_status': form.health_status.data,
                'smoking': form.smoking.data,
                'smoke_freq': form.smoke_freq.data,
                'smoke_per_week': form.smoke_per_week.data,
                'smoker_per_day': form.smoke_per_day.data,
                'smoke_years': form.smoke_years.data,
                'quit_smoke_years': form.quit_smoke_years.data,
                'alcohol': form.alcohol.data,
                'drink_per_day': form.drink_per_day.data,
                'drink_years': form.drink_years.data,
                'quit_drink_years': form.quite_drink_years.data,
                'congenital_disease': form.congenital_disease.data,
                'congenital_dis_other': form.congenital_dis_other.data,
                'congenital_dis_years': form.congenital_dis_years.data,
                'systolic': form.systolic.data,
                'diastolic': form.diastolic.data,
                'smoke_screening': form.smoke_screening.data,
                'bp': form.bp.data,
                'fpg': form.fpg.data,
                'abnormal_lipid': form.abnormal_lipid.data,
                'waist': form.waist.data,
                'infarction': form.infarction.data,
                'family_infarction': form.family_infarction.data,
                'dental_brushing': form.dental_brushing.data,
                'dental_brushing_gt_twice': form.dental_brushing_gt_twice.data,
                'dental_brushing_other': form.dental_brushing_other.data,
                'fluoride_toothpaste': form.fluoride_toothpaste.data,
                'dental_floss': form.dental_floss.data,
                'dental_floss_equip': form.dental_floss_equip.data,
                'smoke_ten_cig': form.smoke_ten_cig.data,
                'chew_gum': form.chew_gum.data,
                'dental_part_two_one': form.dental_part_two_one.data,
                'dental_part_two_two': form.dental_part_two_two.data,
                'dental_part_two_three': form.dental_part_two_three.data,
                'dental_part_two_four': form.dental_part_two_four.data,
                'dental_part_two_five': form.dental_part_two_five.data,
                'dental_part_two_six': form.dental_part_two_six.data,
                'dental_part_two_seven': form.dental_part_two_seven.data,
                'dental_part_two_one_follow_up': form.dental_part_two_one_follow_up.data,
                'dental_part_two_two_follow_up': form.dental_part_two_two_follow_up.data,
                'dental_part_two_three_follow_up': form.dental_part_two_three_follow_up.data,
                'dental_part_two_four_follow_up': form.dental_part_two_four_follow_up.data,
                'dental_part_two_five_follow_up': form.dental_part_two_five_follow_up.data,
                'dental_part_two_six_follow_up': form.dental_part_two_six_follow_up.data,
                'dental_part_two_seven_follow_up': form.dental_part_two_seven_follow_up.data,
                'dental_transfer_tissue': form.dental_transfer_tissue.data,
                'dental_transfer_gum': form.dental_transfer_gum.data,
                'dental_transfer_cavity': form.dental_transfer_cavity.data,
                'dental_transfer_swallow': form.dental_transfer_swallow.data,
                'dental_transfer_denture': form.dental_transfer_denture.data,
                
                'eye_exam_one': form.eye_exam_one.data,
                'eye_exam_two': form.eye_exam_two.data,
                'eye_exam_three': form.eye_exam_three.data,
                'eye_exam_four': form.eye_exam_four.data,
                'eye_exam_five': form.eye_exam_five.data,
                'eye_exam_three_side': form.eye_exam_three_side.data,
                'eye_exam_four_side': form.eye_exam_four_side.data,
                'eye_exam_five_side': form.eye_exam_five_side.data,
                'snellen_left': form.snellen_left.data,
                'snellen_right': form.snellen_right.data,
                
                'amt_one': form.amt_one.data,
                'amt_two': form.amt_two.data,
                'amt_three': form.amt_three.data,
                'amt_four': form.amt_four.data,
                'amt_five': form.amt_five.data,
                'amt_six': form.amt_six.data,
                'amt_seven': form.amt_seven.data,
                'amt_eight': form.amt_eight.data,
                'amt_nine': form.amt_nine.data,
                'amt_ten': form.amt_ten.data,

                'mmse_one_one': form.mmse_one_one.data,
                'mmse_one_two': form.mmse_one_two.data,
                'mmse_one_three': form.mmse_one_three.data,
                'mmse_one_four': form.mmse_one_four.data,

                'mmse_two_one_one': form.mmse_two_one_one.data,
                'mmse_two_one_two': form.mmse_two_one_two.data,
                'mmse_two_one_three': form.mmse_two_one_three.data,
                'mmse_two_one_four': form.mmse_two_one_four.data,
                'mmse_two_one_five': form.mmse_two_one_five.data,

                'mmse_two_two_one': form.mmse_two_two_one,
                'mmse_two_two_two': form.mmse_two_two_two,
                'mmse_two_two_three': form.mmse_two_two_three,
                'mmse_two_two_four': form.mmse_two_two_four.data,
                'mmse_two_two_five': form.mmse_two_two_five.data,

                'mmse_three_flower': form.mmse_three_flower.data,
                'mmse_three_river': form.mmse_three_river.data,
                'mmse_three_train': form.mmse_three_train.data,
                'mmse_three_tree': form.mmse_three_tree.data,
                'mmse_three_sea': form.mmse_three_sea.data,
                'mmse_three_car': form.mmse_three_car.data,

                'mmse_four_one': form.mmse_four_one.data,
                'mmse_four_two': form.mmse_four_two.data,

                'mmse_five_flower': form.mmse_five_flower.data,
                'mmse_five_river': form.mmse_five_river.data,
                'mmse_five_train': form.mmse_five_train.data,
                'mmse_five_tree': form.mmse_five_tree.data,
                'mmse_five_sea': form.mmse_five_sea.data,
                'mmse_five_car': form.mmse_five_car.data,

                'mmse_six_one': form.mmse_six_one.data,
                'mmse_six_two': form.mmse_six_two.data,
                'mmse_six_three': form.mmse_six_three.data,
                'mmse_nine_one': form.mmse_nine_one.data,
                'mmse_ten_one': form.mmse_ten_one.data,
                'mmse_eleven_one': form.mmse_eleven_one.data,

                'q9_one': form.q9_one.data,
                'q9_two': form.q9_two.data,
                'q9_three': form.q9_three.data,
                'q9_four': form.q9_four.data,
                'q9_five': form.q9_five.data,
                'q9_six': form.q9_six.data,
                'q9_seven': form.q9_seven.data,
                'q9_eight': form.q9_eight.data,
                'q9_nine': form.q9_nine.data,

                'knee_pain': form.knee_pain.data,
                'knee_pain_clinic_one': form.knee_pain_clinic_one.data,
                'knee_pain_clinic_two': form.knee_pain_clinic_two.data,
                'knee_pain_clinic_three': form.knee_pain_clinic_three.data,
                'knee_pain_clinic_four': form.knee_pain_clinic_four.data,
                'knee_pain_clinic_five': form.knee_pain_clinic_five.data,

                'tugt': form.tugt.data,
                'urine_holding': form.uring_holding.data,
                'bmi': form.bmi.data,
                'malnutrition_one': form.malnutrition_one.data,
                'malnutrition_two': form.malnutrition_two.data,
                'malnutrition_three': form.malnutrition_three.data,
                'malnutrition_four': form.malnutrition_four.data,
                'malnutrition_five': form.malnutrition_five.data,
                'malnutrition_six': form.malnutrition_six.data,

                'sleeping_one': form.sleeping_one.data,
                'insomnia': form.insomnia.data,
                'oversleep': form.oversleep.data,
                'snore': form.snore.data,
                'dreamwalk': form.dreamwalk.data,
                'sleeping_other': form.sleeping_other.data,
                'sleeping_period_year': form.sleeping_period_year.data,
                'sleeping_period_month': form.sleeping_period_month.data,
                'sleeping_avg_hours': form.sleeping_avg_hours.data,
                'fatique': form.fatique.data,

                'routine_one': form.routine_one.data,
                'routine_two': form.routine_two.data,
                'routine_three': form.routine_three.data,
                'routine_four': form.routine_four.data,
                'routine_five': form.routine_five.data,
                'routine_six': form.routine_six.data,
                'routine_seven': form.routine_seven.data,
                'routine_eight': form.routine_eight.data,
                'routine_nine': form.routine_nine.data,
                'routine_ten': form.routine_ten.data,

                'long_term_care_one_one': form.long_term_care_one_one.data,
                'long_term_care_one_two': form.long_term_care_one_two.data,
                'long_term_care_one_three': form.long_term_care_one_three.data,
                'long_term_care_two_one': form.long_term_care_two_one.data,
                'long_term_care_two_two': form.long_term_care_two_two.data,
                'long_term_care_three_one': form.long_term_care_three_one.data,
                'long_term_care_three_two_one': form.long_term_care_three_two_one.data,
                'long_term_care_three_two_two': form.long_term_care_three_two_two.data,

                'long_term_care_four_one': form.long_term_care_four_one.data,
                'long_term_care_four_two': form.long_term_care_four_two.data,
                'long_term_care_four_three': form.long_term_care_four_three.data,
                'long_term_care_four_four': form.long_term_care_four_four.data,
                'long_term_care_four_five': form.long_term_care_four_five.data,

                'long_term_care_five_one': form.long_term_care_five_one.data,
                'long_term_care_five_two': form.long_term_care_five_two.data,
                'long_term_care_five_three': form.long_term_care_five_three.data,
                'long_term_care_five_four': form.long_term_care_five_four.data,
                'long_term_care_five_five': form.long_term_care_five_five.data,
                'long_term_care_five_six': form.long_term_care_five_six.data,
                'long_term_care_five_seven': form.long_term_care_five_seven.data,
                'long_term_care_five_eight': form.long_term_care_five_eight.data,
                'long_term_care_five_nine': form.long_term_care_five_nine.data,
                'long_term_care_five_ten': form.long_term_care_five_ten.data,
                'long_term_care_five_eleven': form.long_term_care_five_eleven.data,
                'long_term_care_five_twelve': form.long_term_care_five_twelve.data,
                'long_term_care_five_thirteen': form.long_term_care_five_thirteen.data,
                'long_term_care_five_forteen': form.long_term_care_five_forteen.data,
                'long_term_care_five_fifteen': form.long_term_care_five_fifteen.data,
                'long_term_care_five_sixteen': form.long_term_care_five_sixteen.data,

                'locale': current_user.province,
                'update_datetime': insert_datetime,
                'insert_datetime': insert_datetime,
                'updated_by': current_user.username,
                'inserted_by': current_user.username,
                }
        db.form1.insert(form_data, safe=True)
        flash('Data added sucessfully.')
        return redirect(url_for('.form_1_view'))

    return render_template('form_1.html', form=form,
            user=current_user,
            provinces=json_util.dumps(provinces_json),
            provinces_list=json_util.dumps(provinces_json.keys()),
            amphurs=json_util.dumps(amphurs_json))

@main.route('/form_1_view', methods=['GET', 'POST'])
@login_required
def form_1_view():
    return render_template('form_1_report.html', db=db)

@main.route('/get_all_data')
@login_required
def get_all_data():
    # draw = int(request.args.get('draw')) or 1
    # start = int(request.args.get('start')) or 0
    # length = int(request.args.get('length')) or 10
    # search = request.args.get('search') or None
    data = []
    no = 0
    # no = start
    for res in db.form1.find():
        no += 1
        result = [no,
                    res['pid'],
                    res['firstname'],
                    res['lastname'],
                    res['age'],
                    res['district'],
                    res['amphur'],
                    res['province'],
                ]
        data.append(result)

    return jsonify(data=data)

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
