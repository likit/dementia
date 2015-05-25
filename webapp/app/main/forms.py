# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms.validators import Required, NumberRange, Optional
from wtforms import (StringField,
                        SubmitField,
                        IntegerField,
                        SelectField,
                        )

class Form1(Form):
    # Personal info part
    age = IntegerField(u'อายุ', validators=[Required(), NumberRange(1,130)])
    gender = SelectField(u'เพศ', validators=[Required(),],
            choices=[('male',u'ชาย'),
                ('female', u'หญิง'), ('none', u'ไม่ระบุ')])
    marital = SelectField(u'สถานภาพสมรส', validators=[Required(),],
            choices=[('married', u'แต่งงานแล้ว'), ('widow', u'หม้าย'),
                ('divorce', u'หย่าร้าง'), ('single', u'โสด'),
                ('other', u'อื่นๆ')])
    marital_other = StringField(u'อื่นๆ โปรดระบุ')
    edu = SelectField(u'', validators=[Required()],
            choices=[('none', u'ไม่ได้รับการศึกษา'),
                ('elementary', u'ประถมศึกษา'),
                ('middleschool', u'มัธยมศึกษาตอนต้น'),
                ('highschool', u'มัธยมศึกษาตอนปลาย'),
                ('diploma', u'อนุปริญญา'),
                ('bachelor', u'ปริญญาตรี'),
                ('higherbachelor', u'สูงกว่าปริญญาตรี'),
                ('other', u'อื่นๆ')])
    edu_other = StringField(u'อื่นๆ โปรดระบุ')
    edu_years = IntegerField(u'รวมจำนวนปีที่ได้รับการศึกษา')
    living = SelectField(u'การพักอาศัย', validators=[Required()],
            choices=[('single', u'โสด'),
                ('couple', u'กับคู่ครอง'),
                ('family', u'กับครอบครัว'),
                ('caregiver', u'กับผู้ดูแล'),
                ('other', u'อื่นๆ'),
                ])
    living_caregiver = StringField(u'มีผู้ดูแลโปรดระบุ')
    living_other = StringField(u'อื่นๆ โปรดระบุ')
    income = SelectField(u'ท่านคิดว่ามีรายได้เพียงพอในครอบครัว',
            validators=[Required()],
            choices=[
                ('excess', u'เหลือเก็บ'),
                ('enough', u'กำลังพอดี'),
                ('notenough', u'ไม่เพียงพอ'),
                ])

    elder_club = SelectField(u'การเป็นสมาชิกชมรมผู้สูงอายุ/อื่นๆ',
            validators=[Required()],
            choices=[('yes', u'เป็น'), ('no', u'ไม่เป็น')])

    health_status = SelectField(u'ความรู้สึกต่อสุขภาพตนเองโดยรวม',
            validators=[Required()],
            choices=[
                ('excellent', u'ดีเยี่ยม'),
                ('verygood', u'ดีมาก'),
                ('good', u'ดี'),
                ('bad', u'แย่'),
                ('verybad', u'แย่มาก'),
                ])

    smoking = SelectField(u'การสูบบุหรี่/ยาสูบ', validators=[Required()],
            choices=[
                ('no', u'ไม่เคยสูบเลย'),
                ('yes', u'ปัจจุบันยังสูบ'),
                ('quit', u'เคยสูบ (ตอนนี้เลิกแล้ว)'),
                ])

    smoke_freq = SelectField(u'ความถี่',
            choices=[
                ('sometimes', u'บ่อยครั้ง'),
                ('daily', u'ทุกวัน'),
                ])

    smoke_per_week = IntegerField(u'จำนวนมวนต่อสัปดาห์')
    smoke_per_day = IntegerField(u'จำนวนมวนต่อวัน')

    smoke_years = IntegerField(u'เป็นเวลา (ปี)')
    quit_smoke_years = IntegerField(u'เลิกมา (ปี)')

    alcohol = SelectField(u'ดื่มแอลกอฮอล์', validators=[Required()],
            choices=[
                ('none', u'ไม่เคยดื่ม'),
                ('sometimes', u'บางครั้ง'),
                ('daily', u'ทุกวัน'),
                ('quit', u'เคยดื่ม'),
                ])

    drink_per_day = IntegerField(u'จำนวนแก้ว (ต่อวัน)')
    drink_years = IntegerField(u'เป็นเวลา (ปี)')
    quit_drink_years = IntegerField(u'เลิกมา (ปี)')

    congenital_disease = SelectField(u'โรคประจำตัว', validators=[Required()],
            choices=[
                ('none', u'ไม่มีโรคประจำตัว'),
                ('diabetes', u'โรคเบาหวาน'),
                ('hypertension', u'โรคความดันโลหิตสูง'),
                ('hyperlipidemia', u'โรคไขมันในเลือดผิดปกติ'),
                ('heart-disease', u'โรคหัวใจ'),
                ('cancer', u'โรคมะเร็ง'),
                ('obstructive-lung-disease', u'โรคปอดอุดกั้นเรื้อรัง'),
                ('other', u'อื่นๆ'),
                ])

    congenital_dis_other = StringField(u'อื่นๆ โปรดระบุ')
    congenital_dis_years = IntegerField(u'เป็นมาเป็นเวลา (ปี)')

    # Other parts
    submit = SubmitField('Submit')
