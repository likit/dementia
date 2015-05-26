# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms.validators import Required, NumberRange, Optional
from wtforms import (StringField,
                        SubmitField,
                        IntegerField,
                        SelectField,
                        BooleanField,
                        RadioField,
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
    systolic = IntegerField(u'ความดันโลหิตตัวบน หรือซิสโตลิค (SBP)', validators=[Required()])
    diastolic = IntegerField(u'ความดันโลหิตตัวล่าง หรือไดแอสโตลิค (DBP)', validators=[Required()])
    smoke_screening = BooleanField(u'ยังคงสูบบุหรี่ ยาเส้น ยาสูบ บุหรี่ซิกาแรต บุหรี่ซิการ์ หรือหยุดสูบไม่เกิน 1 ปี')
    bp = BooleanField(u'ระดับความดันโลหิต >=130/85 มม.ปรอท และ/หรือ เคยได้รับการวินิจฉัยจากแพทย์ว่าเป็นความดันโลหิตสูง')
    fpg = BooleanField(u'ระดับน้ำตาลในเลือด (FPG) >=100 มก./ดล. และ/หรือ เคยได้รับการวินิจฉัยจากแพทย์ว่าเป็นโรคเบาหวาน')
    abnormal_lipid = BooleanField(u'เคยได้รับการวินิจฉัยจากแพทย์ว่ามีภาวะไขมันเลือดผิดปกติโดย<br>TC >280 มก./ดล. และ/หรือ LDL >100 มก./ดล. และ/หรือ TG >150 มก./ดล. และ/หรือ ในชาย HDL <40 มก./ดล. ในหญิง HDL <50 มก./ดล.')
    waist = BooleanField(u'เส้นรอบเอวมากกว่าส่วนสูง (ซม.) หาร 2')
    infarction = BooleanField(u'เคยได้รับการวินิจฉัยจากแพทย์ว่าเป็นโรคหัวใจขาดเลือด หรืออัมพฤกษ์ อัมพาต')
    family_infarction = BooleanField(u'มีญาติสายตรง (พ่อ แม่ พี่หรือน้องท้องเดียวกัน) ที่แพทย์วินิจฉัยว่าเป็นโรคหัวใจขาดเลือด หรืออัมพฤกษ์ อัมพาต (ผู้ชายเป็นก่อนอายุ 55 ปี ผู้หญิงเป็นก่อนอายุ 65 ปี)')
    dental_brushing = SelectField(u'', validators=[Required()],
            choices=[
                ('none', u'ไม่ได้แปรง/ไม่ได้ใช้แปรงสีฟัน'),
                ('bedtime', u'แปรงวันละ 1 ครั้ง ก่อนนอน'),
                ('twice', u'แปรงวันละ 2 ครั้ง เช้าและก่อนนอน'),
                ('many', u'แปรงมากกว่าวันละ 2 ครั้ง'),
                ('other', u'อื่นๆ'),
                ])
    dental_brushing_gt_twice = IntegerField(u'ระบุ')
    dental_brushing_other = StringField(u'อื่นๆ โปรดระบุ')

    fluoride_toothpaste = BooleanField(u'การใช้ยาสีฟันผสมฟลูโอไรด์ทุกวัน',
            validators=[Required()])
    dental_floss = BooleanField(u'การทำความสะอาดซอกฟันทุกวัน')
    dental_floss_equip = StringField(u'ใช้อุปกรณ์ได้แก่')
    smoke_ten_cig = BooleanField(u'สูบบุหรี่มากกว่า 10 มวนต่อวัน')
    chew_gum = BooleanField(u'เคี้ยวหมากเป็นประจำ')

    dental_part_two_one = RadioField(u'<u>เนื้อเยื่อในช่องปาก</u><br>บริเวณริมฝีปาก แก้ม ลิ้น มีปุ่ม ก้อนเนื้อ มีแผลเรื้อรังหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int)
    dental_part_two_two = RadioField(u'<u>เหงือกและอวัยวะปริทันต์</u><br>บริเวณเหงือกมีเลือดออก มีฝีหนอง ฟันโยกหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int)
    dental_part_two_three = RadioField(u'<u>ฟันผุ</u><br>มีฟันผุเป็นรู เสียวฟัน ฟันหัก ฟันแตกเหลือแต่ตอฟันหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int)
    dental_part_two_four = RadioField(u'<u>ปัญหาการเคี้ยวอาหาร/การกลืน</u><br>มีปัญหาการเคี้ยวอาหารการกลืนหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int)
    dental_part_two_five = RadioField(u'<u>ฟันเทียม</u><br>จำเป็นต้องใส่ฟันเทียมหรือทำฟันเทียมหรือไม่',
            choices=[(0, u'จำเป็น'), (1, u'ไม่จำเป็น')], coerce=int)
    dental_part_two_six = RadioField(u'<u>การได้รับการตรวจหรือรักษาจากทันตบุคลากร</u><br>ท่านเคยได้รับการตรวจหรือรักษาจากทันตบุคลากรหรือไม่',
            choices=[(0, u'เคย'), (1, u'ไม่เคย')], coerce=int)
    dental_part_two_seven = RadioField(u'<u>ความต้องการการรักษาทางทันตกรรม</u><br>ปัจจุบันท่านต้องการการรักษาหรือไม่',
            choices=[(0, u'ต้องการ'), (1, u'ไม่ต้องการ')], coerce=int)

    dental_part_two_one_follow_up = BooleanField(u'ใช่')
    dental_part_two_two_follow_up = BooleanField(u'ใช่')
    dental_part_two_three_follow_up = BooleanField(u'ใช่')
    dental_part_two_four_follow_up = BooleanField(u'ใช่')
    dental_part_two_five_follow_up = BooleanField(u'ใช่')
    dental_part_two_six_follow_up = BooleanField(u'ใช่')
    dental_part_two_seven_follow_up = BooleanField(u'ใช่')

    dental_transfer = SelectField(u'', validators=[Required()],
            choices=[
                ('tissue', u'เนื้อเยื่อในช่องปาก'),
                ('gum', u'เหงือกและอวัยวะปริทันต์'),
                ('cavity', u'ฟันผุ'),
                ('swallow', u'ปัญหาการเคี้ยวอาหาร/การกลืน'),
                ('denture', u'ฟันเทียม'),
                ])

    eye_exam_one = BooleanField(u'นับนิ้วในระยะสามเมตรได้ถูกต้อง<u>น้อยกว่า 3 ใน 4 ครั้ง</u>')
    eye_exam_two = BooleanField(u'อ่านหนังสือพิมพ์หน้าหนึ่งในระยะหนึ่งฟุต<u>ไม่ได้</u>')
    eye_exam_three = BooleanField(u'ปิดตาดูทีละข้าง <u>พบว่า</u> ตามัวคล้ายมีหมอกบัง')
    eye_exam_four = BooleanField(u'ปิดตาดูทีละข้าง <u>พบว่า</u> มองเห็นชัดแต่ตรงกลาง ไม่เห็นรอบข้าง หรือมักเดินชนประตู สิ่งของบ่อยๆ')
    eye_exam_five = BooleanField(u'ปิดตาดูทีละข้าง <u>พบว่า</u> เห็นจุดดำกลางภาพ หรือเห็นภาพบิดเบี้ยว')

    eye_exam_three_side = RadioField(u'', choices=[
        ('left', u'ซ้าย'),
        ('right', u'ขวา'),
        ])
    eye_exam_four_side = RadioField(u'', choices=[
        ('left', u'ซ้าย'),
        ('right', u'ขวา'),
        ])
    eye_exam_five_side = RadioField(u'', choices=[
        ('left', u'ซ้าย'),
        ('right', u'ขวา'),
        ])


    submit = SubmitField('Submit')
