# -*- coding: utf-8 -*-

import os
from datetime import datetime

import numpy as np
import json
import pymongo
from collections import Counter

from flask import (render_template, session, redirect,
                        url_for, flash, jsonify, request)
from bson import json_util
from . import main
from .. import db
from .forms import Form1, PersonalForm
from .. import APP_ROOT, APP_STATIC
from app.models import User
from app.main.models import Elder, AnswerForm

from bson.objectid import ObjectId
from flask.ext.login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
#@login_required
def index():
    return render_template('index.html', user=current_user)

@main.route('/searchpid')
def searchpid():
    qpid = request.args.get('pid')
    res = Elder.query.filter_by(pid=qpid).first()
    if res:
        return jsonify(result='found',
                firstname=res.firstname,
                lastname=res.lastname,
                province=res.province,
                district=res.district,
                district_number=res.moo,
                amphur=res.amphur,
                edu=res.edu,
                gender=res.gender,
                marital=res.marital,
                street_number=res.address,
                )
    else:
        return jsonify(result='notfound')

@main.route('/form_1/', methods=['POST', 'GET'])
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

    # form.amphur.choices = [('', '')] + [(x,x) for x in amphurs_json.keys()]
    # form.district.choices = [('', '')] + [(x,x) for x in districts_list]
    form.amphur.choices = [('', '')]
    form.district.choices = [('', '')]

    if form.validate_on_submit():
        insert_datetime = datetime.utcnow()
        elder = Elder.query.filter_by(pid=form.pid.data).first()

        personal_data = {
                'updated_date': datetime.strptime(
                    form.collectdate.data, '%d/%m/%Y'),
                'firstname': form.firstname.data,
                'lastname': form.lastname.data,
                'pid': form.pid.data,
                'address': form.street_number.data,
                'moo': form.district_number.data,
                'province': form.province.data,
                'amphur': form.amphur.data,
                'district': form.district.data,
                'age': form.age.data,
                'weight': form.weight.data,
                'height': form.height.data,
                'gender': form.gender.data,
                'marital': form.marital.data,
                'marital_other': form.marital_other.data,
                'edu': form.edu.data,
                'edu_other': form.edu_other.data,
                'edu_years': form.edu_years.data,
                }

        if not elder:
            elder = Elder(**personal_data)
        else:
            pass

        form_data = {
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
                'quit_drink_years': form.quit_drink_years.data,
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

                'mmse_two_two_one': form.mmse_two_two_one.data,
                'mmse_two_two_two': form.mmse_two_two_two.data,
                'mmse_two_two_three': form.mmse_two_two_three.data,
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
                'mmse_seven_one': form.mmse_seven_one.data,
                'mmse_eight_one': form.mmse_eight_one.data,
                'mmse_eight_two': form.mmse_eight_two.data,
                'mmse_eight_three': form.mmse_eight_three.data,
                'mmse_nine_one': form.mmse_nine_one.data,
                'mmse_ten_one': form.mmse_ten_one.data,
                'mmse_eleven_one': form.mmse_eleven_one.data,

                'q2_one': form.q2_one.data,
                'q2_two': form.q2_two.data,

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
                'urine_holding': form.urine_holding.data,
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
                'long_term_care_five_fourteen': form.long_term_care_five_fourteen.data,
                'long_term_care_five_fifteen': form.long_term_care_five_fifteen.data,
                'long_term_care_five_sixteen': form.long_term_care_five_sixteen.data,

                'locale': current_user.province,
                'updated_on': insert_datetime,
                'created_on': insert_datetime,
                'updated_by': current_user.username,
                'created_by': current_user.username,
                'collected_date': datetime.strptime(
                                    form.collectdate.data, '%d/%m/%Y'),
                }
        db.session.add(elder)
        db.session.commit()
        answer_form = AnswerForm(**form_data)
        answer_form.elder_id = elder.id
        db.session.add(answer_form)
        db.session.commit()
        flash('Data added successfully.')
        return redirect(url_for('.form_1'))

    return render_template('form_1.html', form=form,
            flash=flash,
            user=current_user,
            provinces=json_util.dumps(provinces_json),
            provinces_list=json_util.dumps(provinces_json.keys()),
            amphurs=json_util.dumps(amphurs_json))


@main.route('/view/all/', methods=['GET', 'POST'])
@login_required
def view_all():
    return render_template('form_1_report.html', db=db)


@main.route('/view/person/<pid>', methods=['GET', 'POST'])
@login_required
def view_person(pid):
    data = []
    no = 0
    elder = Elder.query.filter_by(pid=pid).first()

    #TODO: uncomment the line below
    # for res in AnswerForm.query.filter_by(elder_id=elder.id,
    #         locale=current_user.province):
    for res in AnswerForm.query.filter_by(elder_id=elder.id):
        no += 1
        result = [no,
                  elder.pid,
                  elder.firstname,
                  elder.lastname,
                  elder.age,
                  elder.district,
                  elder.amphur,
                  elder.province,
                  str(res.collected_date.date()),
                  ]
        data.append(result)

    return render_template('form_1_person.html', data=data)


@main.route('/view/result', methods=['GET', 'POST'])
@login_required
def view_result():
    pid = request.args.get('pid')
    collectdate = request.args.get('collectdate')
    elder = Elder.query.filter_by(pid=pid).first()
    form = Form1(request.form)

    #TODO: uncomment the line below
    # for f in AnswerForm.query.filter_by(elder_id=elder.id,
    #         locale=current_user.province):
    for f in AnswerForm.query.filter_by(elder_id=elder.id):
        if collectdate == str(f.collected_date.date()):
            break

    na = u'ไม่มีข้อมูล'
    try:
        infarction_score = int(f.smoke_screening) + \
                int(f.bp) + int(f.fpg) + \
                int(f.abnormal_lipid) + \
                int(f.waist) + int(f.infarction) + \
                int(f.family_infarction)
    except:
        infarction_result = None
        infarction_score = None
    else:
        if infarction_score <= 2:
            infarction_result = u'มีความเสี่ยง'
        elif infarction_score < 5:
            infarction_result = u'มีความเสี่ยงสูง'
        elif infarction_score >= 5:
            infarction_result = u'มีความเสี่ยงสูงมาก'

    try:
        dental_hygiene_score = int(f.dental_part_two_one) + \
                    int(f.dental_part_two_two) + \
                    int(f.dental_part_two_three) + \
                    int(f.dental_part_two_four)
    except:
        dental_hygiene_score = None

    try:
        eye_exam_score = int(f.eye_exam_one) + \
                int(f.eye_exam_two) + \
                int(f.eye_exam_three) + \
                int(f.eye_exam_four) + \
                int(f.eye_exam_five)
    except:
        eye_exam_score = None

    try:
        amt_score = int(f.amt_one) + \
                    int(f.amt_two) + \
                    int(f.amt_three) + \
                    int(f.amt_four) + \
                    int(f.amt_five) + \
                    int(f.amt_six) + \
                    int(f.amt_seven) + \
                    int(f.amt_eight) + \
                    int(f.amt_nine) + \
                    int(f.amt_ten)
    except:
        amt_result = None
        amt_score = None
    else:
        if amt_score and amt_score < 8:
            amt_result = u'ผิดปกติ'
        elif amt_score:
            amt_result = u'ปกติ'
        else:
            amt_result = None

    mmses = dict([('correct', 1), ('wrong', 0), ('na', 0)])
    try:
        mmse_score = mmses[f.mmse_one_one] + \
                        mmses[f.mmse_one_two] + \
                        mmses[f.mmse_one_three] + \
                        mmses[f.mmse_one_four] + \
                        mmses[f.mmse_two_one_one] + \
                        mmses[f.mmse_two_one_two] + \
                        mmses[f.mmse_two_one_three] + \
                        mmses[f.mmse_two_one_four] + \
                        mmses[f.mmse_two_one_five] + \
                        mmses[f.mmse_two_two_one] + \
                        mmses[f.mmse_two_two_two] + \
                        mmses[f.mmse_two_two_three] + \
                        mmses[f.mmse_two_two_four] + \
                        mmses[f.mmse_two_two_five]

        if (f.mmse_three_flower or
                f.mmse_three_river or
                f.mmse_three_train):
            mmse_score += int(f.mmse_three_flower) +\
                            int(f.mmse_three_river) + \
                            int(f.mmse_three_train)
        elif (f.mmse_three_tree or
                f.mmse_three_sea or
                f.mmse_three_car):
            mmse_score += int(f.mmse_three_tree) +\
                            int(f.mmse_three_sea) + \
                            int(f.mmse_three_car)

        mmse_score += mmses[f.mmse_four_one] + \
                        mmses[f.mmse_four_two]

        if (f.mmse_five_flower or
                f.mmse_five_river or
                f.mmse_five_train):
            mmse_score += int(f.mmse_five_flower) +\
                            int(f.mmse_five_river) + \
                            int(f.mmse_five_train)
        elif (f.mmse_five_tree or
                f.mmse_five_sea or
                f.mmse_five_car):
            mmse_score += int(f.mmse_five_tree) + \
                            int(f.mmse_five_sea) + \
                            int(f.mmse_five_car)

        mmse_score += mmses[f.mmse_six_one] + \
                        mmses[f.mmse_six_two] + \
                        mmses[f.mmse_seven_one]

        mmse_score += int(f.mmse_eight_one) + \
                        int(f.mmse_eight_two) + \
                        int(f.mmse_eight_three)

        mmse_score += int(f.mmse_nine_one) + \
                        int(f.mmse_ten_one)
    except:
        mmse_result = None
        mmse_score = None
    else:
        if f.edu == 0 and mmse_score <= 14:
            mmse_result = u'เข้าข่ายมีภาวะความจำเสื่อม'
        elif f.edu == 1 and mmse_score <= 17:
            mmse_result = u'เข้าข่ายมีภาวะความจำเสื่อม'
        elif f.edu > 1 and mmse_score <= 22:
            mmse_result = u'เข้าข่ายมีภาวะความจำเสื่อม'
        else:
            mmse_result = u'ปกติ'

    try:
        q2_score = int(f.q2_one) + int(f.q2_two)
    except:
        q2_result = None
        q2_score = None
    else:
        if q2_score == 0:
            q2_result = u'ปกติ'
        else:
            q2_result = u'ผิดปกติ'

    try:
        q9_score = int(f.q9_one) + \
                        int(f.q9_two) + \
                        int(f.q9_three) + \
                        int(f.q9_four) + \
                        int(f.q9_five) + \
                        int(f.q9_six) + \
                        int(f.q9_seven) + \
                        int(f.q9_eight) + \
                        int(f.q9_nine)
    except:
        q9_result = None
        q9_score = None
    else:
        if q9_score < 7:
            q9_result = u'ปกติ'
        elif q9_score >=7 and q9_score < 13:
            q9_result = u'มีอาการของโรคซึมเศร้าระดับน้อย'
        elif q9_score >= 13 and q9_score < 19:
            q9_result = u'มีอาการของโรคซึมเศร้าระดับปานกลาง'
        else:
            q9_result = u'มีอาการของโรคซึมเศร้าระดับมาก'

    if f.knee_pain == 0:
        knee_pain = u'ไม่ปวดเข่า'
    else:
        knee_pain = u'ปวดเข่า'

    try:
        knee_pain_clinic_score = int(f.knee_pain_clinic_one) + \
                                    int(f.knee_pain_clinic_two) + \
                                    int(f.knee_pain_clinic_three) + \
                                    int(f.knee_pain_clinic_four) + \
                                    int(f.knee_pain_clinic_five)
    except:
        knee_pain_clinic = None
        knee_pain_clinic_score = None
    else:
        if knee_pain_clinic_score > 2:
            knee_pain_clinic = u'เสี่ยงต่อโรคข้อเข่าเสื่อม'
        else:
            knee_pain_clinic = u'ปกติ'

    tugt = dict([(0, u'<30 วินาที'),
                (1, u'>=30 วินาที'),
                (2, u'เดินไม่ได้')]).get(f.tugt)

    try:
        urine = dict([(0, u'ไม่มี'), (1, u'มี')]).get(f.urine_holding)
    except:
        urine = None

    try:
        bmi = dict([(0, '<18.5'),
                (1, '18.5-22.9'),
                (2, '23.0-24.9'),
                (3, '25.0-29.9'),
                (4, '>=30')]).get(f.bmi)
    except:
        bmi = None

    try:
        malnutrition_score = int(f.malnutrition_one) + \
                                int(f.malnutrition_two) + \
                                int(f.malnutrition_three) + \
                                int(f.malnutrition_four) + \
                                int(f.malnutrition_five)
    except:
        malnutrition = None
        malnutrition_score = None
    else:
        if malnutrition_score <= 7:
            malnutrition = u'ขาดสารอาหาร'
        elif malnutrition_score > 7 and malnutrition_score <= 11:
            malnutrition = u'เสี่ยงต่อการขาดสารอาหาร'
        else:
            malnutrition = u'ปกติ'

    if f.sleeping_one:
        sleeping = dict([(0, u'ไม่มีปัญหา'), (1, u'มีปัญหา')])[f.sleeping_one]
    else:
        sleeping = u''

    try:
        routine_score = int(f.routine_one) + \
                            int(f.routine_two) + \
                            int(f.routine_three) + \
                            int(f.routine_four) + \
                            int(f.routine_five) + \
                            int(f.routine_six) + \
                            int(f.routine_seven) + \
                            int(f.routine_eight) + \
                            int(f.routine_nine) + \
                            int(f.routine_ten)
    except:
        routine = None
        routine_score = None
    else:
        if routine_score >= 12:
            routine = u'ช่วยเหลือตัวเองได้ และ/หรือช่วยเหลือผู้อื่นและคนในสังคมได้'
        elif routine_score < 12 and routine_score >= 5:
            routine = u'ช่วยเหลือและดูแลตัวเองได้บ้าง'
        else:
            routine = u'ช่วยเหลือตัวเองไม่ได้'

    try:
        long_term_one_prelim_score = int(f.long_term_care_one_one) + \
                                        int(f.long_term_care_one_two) + \
                                        int(f.long_term_care_one_three)
    except:
        long_term_one_prelim_score = None

    try:
        long_term_two_prelim_score = int(f.long_term_care_two_one) + \
                                        int(f.long_term_care_two_two)
    except:
        long_term_two_prelim_score = None

    try:
        long_term_three_prelim_score = int(f.long_term_care_three_one)
        long_term_three_prelim_score += \
                                1 if f.long_term_care_three_two_one and \
                                    f.long_term_care_three_two_two else 0
    except:
        long_term_three_prelim_score = None

    try:
        long_term_four_prelim_score = int(f.long_term_care_four_one) + \
                                        int(f.long_term_care_four_two) + \
                                        int(f.long_term_care_four_three) + \
                                        int(f.long_term_care_four_four) + \
                                        int(f.long_term_care_four_five)
    except:
        long_term_four_prelim_score = None

    try:
        long_term_five_prelim_score = int(f.long_term_care_five_one) + \
                                        int(f.long_term_care_five_two) + \
                                        int(f.long_term_care_five_three) + \
                                        int(f.long_term_care_five_four) + \
                                        int(f.long_term_care_five_five) + \
                                        int(f.long_term_care_five_six) + \
                                        int(f.long_term_care_five_seven) + \
                                        int(f.long_term_care_five_eight) + \
                                        int(f.long_term_care_five_nine) + \
                                        int(f.long_term_care_five_ten) + \
                                        int(f.long_term_care_five_eleven) + \
                                        int(f.long_term_care_five_twelve) + \
                                        int(f.long_term_care_five_thirteen) + \
                                        int(f.long_term_care_five_fourteen) + \
                                        int(f.long_term_care_five_fifteen) + \
                                        int(f.long_term_care_five_sixteen)
    except:
        long_term_five_prelim_score = None

    if long_term_one_prelim_score != None:
        if long_term_one_prelim_score <= 3:
            long_term_one_score = 0
    else:
        long_term_one_score = None

    if long_term_two_prelim_score != None:
        if long_term_two_prelim_score == 0:
            long_term_two_score = 1
        if long_term_two_prelim_score == 1:
            long_term_two_score = 2
        if long_term_two_prelim_score == 2:
            long_term_two_score = 3
    else:
        long_term_two_score = None

    if long_term_three_prelim_score != None:
        if long_term_three_prelim_score == 0:
            long_term_three_score = 2
        if long_term_three_prelim_score == 1:
            long_term_three_score = 4
        if long_term_three_prelim_score == 2:
            long_term_three_score = 6
    else:
        long_term_three_score = None

    if long_term_four_prelim_score != None:
        if long_term_four_prelim_score == 0:
            long_term_four_score = 0
        if (long_term_four_prelim_score == 1 or
                long_term_four_prelim_score == 2):
            long_term_four_score = 8
        if (long_term_four_prelim_score >= 3 and
                long_term_four_prelim_score <= 5):
            long_term_four_score = 12
    else:
        long_term_four_score = None

    if long_term_five_prelim_score != None:
        if (long_term_five_prelim_score >= 16 and
                long_term_five_prelim_score <= 20):
            long_term_five_score = 6
        if (long_term_five_prelim_score >= 21 and
                long_term_five_prelim_score <= 35):
            long_term_five_score = 12
        if (long_term_five_prelim_score >= 36 and
                long_term_five_prelim_score <= 48):
            long_term_five_score = 18
    else:
        long_term_five_score = None

    try:
        long_term_score_total = long_term_one_score + \
                                    long_term_two_score + \
                                    long_term_three_score + \
                                    long_term_four_score + \
                                    long_term_five_score
    except:
        long_term = None
        long_term_score_total = None
    else:
        if long_term_score_total >= 0 and long_term_score_total <= 16:
            long_term = u'ไม่ต้องการการดูแลระยะยาว'
        if long_term_score_total >= 17 and long_term_score_total <= 19:
            long_term = u'ต้องเผ้าระวัง'
        if long_term_score_total >= 20:
            long_term = u'ต้องการการดูแลระยะยาว'

    incomplete = u'ข้อมูลไม่พอสำหรับการแปลผล'
    return render_template('show_personal_data.html',
            person=elder,
            genders=dict(form.gender.choices),
            maritals=dict(form.marital.choices),
            edus=dict(form.edu.choices),
            livings=dict(form.living.choices),
            incomes=dict(form.income.choices),
            clubs=dict(form.elder_club.choices),
            health_statuses=dict(form.health_status.choices),
            smokings=dict(form.smoking.choices),
            smoke_freqs=dict(form.smoke_freq.choices),
            alcohols=dict(form.alcohol.choices),
            congenital_diseases=dict(form.congenital_disease.choices),
            infarction_result=infarction_result,
            infarction_score=infarction_score,
            dental_hygiene_score=dental_hygiene_score,
            eye_exam_score=eye_exam_score,
            amt_result=amt_result,
            amt_score=amt_score,
            mmse_result=mmse_result,
            mmse_score=mmse_score,
            q2_score=q2_score,
            q2_result=q2_result,
            q9_score=q9_score,
            q9_result=q9_result,
            knee_pain=knee_pain,
            knee_pain_clinic_score=knee_pain_clinic_score,
            knee_pain_clinic=knee_pain_clinic,
            tugt=tugt,
            urine=urine,
            bmi=bmi,
            malnutrition_score=malnutrition_score,
            malnutrition=malnutrition,
            sleeping=sleeping,
            routine_score=routine_score,
            routine=routine,
            long_term_score_total=long_term_score_total,
            long_term=long_term,
            na=na,
            incomplete=incomplete,
            )


@main.route('/get_person_data')
@login_required
def get_person_data():
    pid = request.args.get('pid')
    # start = int(request.args.get('start')) or 0
    # length = int(request.args.get('length')) or 10
    # search = request.args.get('search') or None
    data = []
    no = 0
    # no = start
    for res in db.form1.find({'pid': pid}):
        no += 1
        try:
            result = [no,
                      res['pid'],
                      res['firstname'],
                      res['lastname'],
                      res['age'],
                      res['district'],
                      res['amphur'],
                      res['province'],
                      str(res['created_date'].date()),
                      ]
        except:
            pass
        else:
            data.append(result)

    return jsonify(data=data)


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
    # for res in Elder.query.filter_by(province=current_user.province):
    for res in Elder.query.all():
        no += 1
        try:
            result = [no,
                        res.pid,
                        res.firstname,
                        res.lastname,
                        res.age,
                        res.district,
                        res.amphur,
                        res.province,
                        str(res.updated_date.date()),
                    ]
        except:
            pass
        else:
            data.append(result)

    return jsonify(data=data)

@main.route('/your_account/')
@login_required
def your_account_view():
    user = User.query.filter_by(username=current_user.username).first()
    return render_template('your_account.html', db=db, user=user)

@main.route('/viz/<year>')
@login_required
def age_viz(year):
    '''Visualize ages in a pie chart.'''
    males = 0
    females = 0
    others = 0
    male_ages = [0]  # add zero so the list is not empty
    female_ages = [0]  # empty list fails to draw the boxplot
    other_ages = [0]
    if current_user.username == 'admin':  # TEMPORARY
        cursor = AnswerForm.query.all()
    else:
        # cursor = AnswerForm.query.filter_by(locale=current_user.province)
        cursor = AnswerForm.query.all()

    n = 0
    for rec in cursor:
        elder = Elder.query.get(rec.elder_id)
        if year != 'all':
            try:
                eyear = rec.collected_date.year
            except:
                continue
            else:
                if eyear != int(year):
                    continue
        n += 1

        if elder.gender == u'ชาย':
            males += 1
            if elder.age:
                male_ages.append(elder.age)
        elif elder.gender == u'หญิง':
            females += 1
            if elder.age:
                female_ages.append(elder.age)
        else:
            others += 1
            if elder.age:
                other_ages.append(elder.age)

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
        outliers = np.concatenate((data[data>upper_whisker], data[data<lower_whisker]))

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
            boxplotdata=boxplotdata, year=year, total=n)

@main.route('/viz/knee/<year>')
@login_required
def knee_viz(year):
    '''Visualize knee pain in a pie chart.'''
    # Should categorize based on genders
    pain = 0
    no_pain = 0
    others = 0
    na = 0
    pain_prov = []
    no_pain_prov = []
    if current_user.username == 'admin':  # TEMPORARY
        cursor = AnswerForm.query.all()
    else:
        # cursor = AnswerForm.query.filter_by(locale=current_user.province)
        cursor = AnswerForm.query.all()

    n = 0
    for rec in cursor:
        if year != 'all':
            try:
                eyear = rec.created_date.year
            except:
                continue
            else:
                if eyear != int(year):
                    continue
        n += 1
        #TODO: find out whether we want locale or province
        if rec.knee_pain == 1:
            pain += 1
            try:
                pain_prov.append(rec.locale)
            except:
                pain_prov.append('Unknown')
        elif rec.knee_pain == 0:
            no_pain += 1
            try:
                no_pain_prov.append(rec.locale)
            except:
                no_pain_prov.append('Unknown')
        else:
            others += 1

    piedata = [{'key': 'ปวดเข่า', 'y': pain},
               {'key': 'ไม่ปวดเข่า', 'y': no_pain},
               {'key': 'ไม่มีข้อมูล', 'y': na},
               {'key': 'อืนๆ', 'y': others},
               ]
    pain_prov = Counter(pain_prov)
    no_pain_prov = Counter(no_pain_prov)
    return render_template('viz/knee.html', piedata=piedata, total=n, year=year,
                           pain=pain, no_pain=no_pain, na=na, others=others,
                           pain_prov=pain_prov, no_pain_prov=no_pain_prov)

@main.route('/viz/longterm/<year>')
@login_required
def longterm_viz(year):
    longterm_two_scores = dict([(0, 0), (1, 0), (2, 0), (3, 1), (4, 1), (5, 1)])
    na = 0
    need = []
    no_need = []
    if current_user.username == 'admin':  # TEMPORARY
        cursor = AnswerForm.query.all()
    else:
        # cursor = AnswerForm.query.filter_by(locale=current_user.province)
        cursor = AnswerForm.query.all()

    n = 0
    scores = []
    for rec in cursor:
        if year != 'all':
            try:
                eyear = rec.created_date.year
            except:
                continue
            else:
                if eyear != int(year):
                    continue
        score = 0
        n += 1
        try:
            social_score = 0
            social_score += rec.long_term_care_one_one
            social_score += rec.long_term_care_one_two
            social_score += rec.long_term_care_one_three

            sense_score = 0
            sense_score += longterm_two_scores[rec.long_term_care_two_one]
            sense_score += longterm_two_scores[rec.long_term_care_two_two]

            depress_score = 0
            depress_score += rec.long_term_care_three_one
            if (rec.long_term_care_three_two_one or
                    rec.long_term_care_three_two_two):
                depress_score += 1

            sensitive_score = 0
            sensitive_score += int(rec.long_term_care_four_one)
            sensitive_score += int(rec.long_term_care_four_two)
            sensitive_score += int(rec.long_term_care_four_three)
            sensitive_score += int(rec.long_term_care_four_four)
            sensitive_score += int(rec.long_term_care_four_five)

            routine_score = 0
            routine_score += rec.long_term_care_five_one + 1
            routine_score += rec.long_term_care_five_two + 1
            routine_score += rec.long_term_care_five_three + 1
            routine_score += rec.long_term_care_five_four + 1
            routine_score += rec.long_term_care_five_five + 1
            routine_score += rec.long_term_care_five_six + 1
            routine_score += rec.long_term_care_five_seven + 1
            routine_score += rec.long_term_care_five_eight + 1
            routine_score += rec.long_term_care_five_nine + 1
            routine_score += rec.long_term_care_five_ten + 1
            routine_score += rec.long_term_care_five_eleven + 1
            routine_score += rec.long_term_care_five_twelve + 1
            routine_score += rec.long_term_care_five_thirteen + 1
            routine_score += rec.long_term_care_five_fourteen + 1
            routine_score += rec.long_term_care_five_fifteen + 1
            routine_score += rec.long_term_care_five_sixteen + 1

            total_score = 0
            if social_score <= 3:
                total_score += 0
            total_score += sense_score + 1
            if depress_score == 0:
                total_score += 2
            if depress_score == 1:
                total_score += 4
            if depress_score == 2:
                total_score += 6
            if sensitive_score == 0:
                total_score += 4
            if sensitive_score >=1 and sensitive_score <= 2:
                total_score += 8
            if sensitive_score >=3 and sensitive_score <= 5:
                total_score += 12
            if routine_score >=16 and routine_score <= 20:
                total_score += 6
            if routine_score >=21 and routine_score <= 35:
                total_score += 12
            if routine_score >=36 and routine_score <= 48:
                total_score += 18

        except:
            na += 1
            continue
        try:
            scores.append((rec.locale,total_score))
        except KeyError:
            continue

    noneed = len([x[1] for x in scores if x[1] <= 16])
    watch = len([x[1] for x in scores if x[1] >= 17 and x[1] <= 19])
    need = len([x[1] for x in scores if x[1] > 20])
    noneed_prov = Counter([x[0] for x in scores if x[1] <= 16])
    watch_prov = Counter([x[0] for x in scores if x[1] >= 17 and x[1] <= 19])
    need_prov = Counter([x[0] for x in scores if x[1] > 20])

    piedata = [{'key': 'ต้องการ', 'y': need},
               {'key': 'ไม่ต้องการ', 'y': noneed},
               {'key': 'เฝ้าระวัง', 'y': watch},
               {'key': 'ไม่มีข้อมูล', 'y': na},
               {'key': 'อืนๆ', 'y': 0},
               ]
    return render_template('viz/longterm.html',
               piedata=piedata, total=n, year=year, na=na, noneed=noneed, need=need, watch=watch,
               noneed_prov=noneed_prov, need_prov=need_prov, watch_prov=watch_prov)


@main.route('/viz/mmse/<year>')
@login_required
def mmse_viz(year):
    na = 0
    positive = 0
    negative = 0
    if current_user.username == 'admin':  # TEMPORARY
        cursor = db.form1.find()
    else:
        cursor = db.form1.find({'province': current_user.province})

    n = 0
    scores = []
    for rec in cursor:
        if year != 'all':
            try:
                eyear = rec['created_date'].year
            except:
                continue
            else:
                if eyear != int(year):
                    continue
        score = 0
        n += 1
        try:
            if rec['mmse_one_one'] == 1: score += 1
            if rec['mmse_one_two'] == 1: score += 1
            if rec['mmse_one_three'] == 1: score += 1
            if rec['mmse_one_four'] == 1: score += 1
            if rec['mmse_one_five'] == 1: score += 1
            if rec['mmse_two_one_one'] == 1: score += 1
            if rec['mmse_two_one_two'] == 1: score += 1
            if rec['mmse_two_one_three'] == 1: score += 1
            if rec['mmse_two_one_four'] == 1: score += 1
            if rec['mmse_two_one_five'] == 1: score += 1
            if rec['mmse_two_two_one'] == 1: score += 1
            if rec['mmse_two_two_two'] == 1: score += 1
            if rec['mmse_two_two_three'] == 1: score += 1
            if rec['mmse_two_two_four'] == 1: score += 1
            if rec['mmse_two_two_five'] == 1: score += 1

            itemscore = 0
            itemscore += int(rec['mmse_three_flower'])
            itemscore += int(rec['mmse_three_river'])
            itemscore += int(rec['mmse_three_train'])
            if itemscore == 0:
                itemscore += int(rec['mmse_three_tree'])
                itemscore += int(rec['mmse_three_sea'])
                itemscore += int(rec['mmse_three_car'])
            score += itemscore

            if rec['edu'] > 1:
                if rec['mmse_four_one'] < 6:
                    score += rec['mmse_four_one']

                if rec['mmse_four_two'] < 6:
                    score += rec['mmse_four_two']

            itemscore = 0
            itemscore += int(rec['mmse_five_flower'])
            itemscore += int(rec['mmse_five_river'])
            itemscore += int(rec['mmse_five_train'])
            if itemscore == 0:
                itemscore += int(rec['mmse_five_tree'])
                itemscore += int(rec['mmse_five_sea'])
                itemscore += int(rec['mmse_five_car'])
            score += itemscore

            if rec['mmse_six_one'] == 1:
                score += 1
            if rec['mmse_six_two'] == 1:
                score += 1
            if rec['mmse_seven_one'] == 1:
                score += 1

            score += int(rec['mmse_eight_one'])
            score += int(rec['mmse_eight_two'])
            score += int(rec['mmse_eight_three'])
            if rec['edu'] > 1:
                score += int(rec['mmse_nine_one'])
                score += int(rec['mmse_ten_one'])
            score += int(rec['mmse_eleven_one'])

            if rec['edu'] == 1 and score <= 14:
                positive += 1
            elif rec['edu'] == 2 and score <= 17:
                positive += 1
            elif rec['edu'] > 2 and score <= 22:
                positive += 1
            else:
                negative += 1
        except:
            na += 1

    piedata = [{'key': u'สงสัยภาวะสมองเสื่อม', 'y': positive},
               {'key': u'ปกติ', 'y': negative},
               {'key': u'ไม่มีข้อมูล', 'y': na},
           ]
    return render_template('viz/mmse.html', piedata=piedata, total=n, year=year)

@main.route('/edit_info', methods=['POST', 'GET'])
def edit_info():
    qpid = request.args.get('qpid')
    elder = Elder.query.filter_by(pid=qpid).first()
    form = PersonalForm(obj=elder)
    if form.validate_on_submit():
        form.populate_obj(elder)
        # db.session.add()
        #TODO: Add eror handler here
        db.session.commit()
        flash('บันทึกข้อมูลเรียบร้อยแล้ว')
        return redirect(url_for('main.view_person', pid=elder.pid))
    return render_template('info_form.html', form=form, elder=elder)
