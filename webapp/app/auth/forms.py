# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms import (StringField, PasswordField,
                        BooleanField, SubmitField, IntegerField,
                        SelectField, TextAreaField)
from wtforms.validators import (Required, Email, Length,
                                    Regexp, EqualTo, Optional)
from wtforms.widgets import Select
from wtforms import ValidationError
from .. import db

import sys

class LoginForm(Form):
    pid = StringField(u'รหัสบัตรประชาชน', validators=[Required(), Length(1, 13,
                message=u'รหัสบัตรประชาชนต้องมี 13 หลัก')])
    password = PasswordField(u'รหัสผ่าน',
            validators=[Required()])
    remember_me = BooleanField(u'จดจำบัญชีนี้ไว้')
    submit = SubmitField(u'ลงชื่อเข้าใช้')

class RegistrationForm(Form):
    pid = StringField(u'รหัสบัตรประชาชน', validators=[Required()])
    password = PasswordField(u'รหัสผ่าน', validators=[
        Required(), EqualTo('password2', message=u'รหัสผ่านต้องตรงกัน')])
    password2 = PasswordField(u'รหัสผ่านอีกครั้ง', validators=[Required()])
    title = SelectField(u'คำนำหน้า',
            choices=[(u'นาย',u'นาย'), (u'นาง',u'นาง'), (u'น.ส.', u'น.ส.')],
            validators=[Required()])
    name = StringField(u'ชื่อ', validators=[Required()])
    lastname = StringField(u'นามสกุล', validators=[Required()])
    position = StringField(u'ตำแหน่ง', validators=[Required()])
    phone = StringField(u'โทรศัพท์', validators=[Required()])
    cell = StringField(u'มือถือ', validators=[Optional()])

    org = StringField(u'องค์กร', validators=[Required()])
    org_address = StringField(u'เลขที่', validators=[Required()])
    mhoo = StringField(u'หมู่', validators=[Required()])
    province = SelectField(u'จังหวัด')
    amphur = SelectField(u'อำเภอ')
    district = SelectField(u'ตำบล')
    objective = TextAreaField(u'วัตถุประสงค์', validators=[Optional()])

    submit = SubmitField(u'ลงทะเบียน')

    # def validate_email(self, field):
    #     if db.users.find_one({'email': field.data}):
    #         raise ValidationError('Email already registered.')

    def validate_pid(self, field):
        if db.users.find_one({'pid': field.data}):
            raise ValidationError('PID already registered.')
