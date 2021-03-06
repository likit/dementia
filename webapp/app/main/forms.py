# coding: utf-8

from flask.ext.wtf import Form
from wtforms.validators import (Required, NumberRange, Optional, Length)
from wtforms import (StringField,
                        SubmitField,
                        IntegerField,
                        SelectField,
                        BooleanField,
                        RadioField,
                        DecimalField,
                        )

class NotValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass

class PersonalForm(Form):
    #TODO: Change street_number and district_number to address and moo
    # in other forms
    # For editing some personal information
    firstname = StringField(u'ชื่อ', validators=[Required()])
    lastname = StringField(u'นามสกุล', validators=[Required()])
    # pid = StringField(u'รหัสบัตรประชาชน', validators=[Required()])
    address = StringField(u'บ้านเลขที่', validators=[Required()])
    moo = StringField(u'หมู่', validators=[Required()])
    age = IntegerField(u'อายุ', validators=[NumberRange(1,130), Optional()])
    weight = StringField(u'น้ำหนัก', validators=[Optional()])
    height = StringField(u'ส่วนสูง', validators=[Optional()])
    submit = SubmitField()

class Form1(Form):
    # Personal info part
    collectdate = StringField(u'', validators=[Required()])
    firstname = StringField(u'ชื่อ', validators=[Required()])
    lastname = StringField(u'นามสกุล', validators=[Required()])
    pid = StringField(u'รหัสบัตรประชาชน', validators=[Required()])
    street_number = StringField(u'บ้านเลขที่', validators=[Required()])
    district_number = StringField(u'หมู่', validators=[Required()])
    province = SelectField(u'จังหวัด', validators=[Required()], coerce=unicode)
    amphur = NotValidatingSelectField(u'อำเภอ', validators=[Required()], coerce=unicode)
    district = NotValidatingSelectField(u'ตำบล', validators=[Required()], coerce=unicode)
    age = IntegerField(u'อายุ', validators=[NumberRange(1,130), Optional()])
    weight = StringField(u'น้ำหนัก', validators=[Optional()])
    height = StringField(u'ส่วนสูง', validators=[Optional()])
    gender = SelectField(u'เพศ', validators=[Optional()],
            choices=[('', u'โปรดเลือก'),
                        (u'ชาย',u'ชาย'),
                        (u'หญิง', u'หญิง'),
                        (u'ไม่ระบุ', u'ไม่ระบุ')], default='')
    marital = SelectField(u'สถานภาพสมรส', validators=[Optional()],
            choices=(('', u'โปรดเลือก'),
                     (u'แต่งงานแล้ว', u'แต่งงานแล้ว'),
                     (u'หม้าย', u'หม้าย'),
                     (u'หย่าร้าง', u'หย่าร้าง'),
                     (u'โสด', u'โสด'),
                     (u'สมณะ', u'สมณะ'),
                     (u'อื่นๆ', u'อื่นๆ')), default='')
    marital_other = StringField(u'อื่นๆ โปรดระบุ', validators=[Optional()])
    edu = SelectField(u'ระดับการศึกษา', validators=[Optional()],
            choices=[(-1, u'โปรดเลือก'),
                (1, u'ไม่ได้ศึกษา/ไม่มีวุฒิการศึกษา'),
                (2, u'ประถมศึกษา'),
                (3, u'มัธยมศึกษาตอนต้น'),
                (4, u'มัธยมศึกษาตอนปลาย หรือ ปวช.'),
                (7, u'อนุปริญญา ปวท.,ปวช.'),
                (5, u'ระดับปริญญาตรี'),
                (6, u'สูงกว่าปริญญาตรี'),
                (0, u'ไม่ระบุ/ไม่ทราบ'),
                (8, u'อื่นๆ')], coerce=int, default=-1)
    edu_other = StringField(u'อื่นๆ โปรดระบุ', validators=[Optional()])
    edu_years = IntegerField(u'รวมจำนวนปีที่ได้รับการศึกษา', validators=[Optional()])
    living = SelectField(u'การพักอาศัย', validators=[Optional()],
            choices=[('', u'โปรดเลือก'),
                (u'โสด', u'โสด'),
                (u'กับคู่ครอง', u'กับคู่ครอง'),
                (u'กับครอบครัว', u'กับครอบครัว'),
                (u'กับผู้ดูแล', u'กับผู้ดูแล'),
                (u'อื่นๆ', u'อื่นๆ')], default='')
    living_caregiver = StringField(u'มีผู้ดูแลโปรดระบุ', validators=[Optional()])
    living_other = StringField(u'อื่นๆ โปรดระบุ', validators=[Optional()])
    income = SelectField(u'ท่านคิดว่ามีรายได้เพียงพอในครอบครัว',
            choices=[
                ('excess', u'เหลือเก็บ'),
                ('enough', u'กำลังพอดี'),
                ('notenough', u'ไม่เพียงพอ'),
                ], validators=[Optional()])

    elder_club = SelectField(u'การเป็นสมาชิกชมรมผู้สูงอายุ/อื่นๆ',
            choices=[('', u'โปรดเลือก'),
                    ('yes', u'เป็น'),
                    ('no', u'ไม่เป็น')],
                    validators=[Optional()], default='')

    health_status = SelectField(u'ความรู้สึกต่อสุขภาพตนเองโดยรวม',
            choices=[('', u'โปรดเลือก'),
                ('excellent', u'ดีเยี่ยม'),
                ('verygood', u'ดีมาก'),
                ('good', u'ดี'),
                ('bad', u'แย่'),
                ('verybad', u'แย่มาก'),
                ], default='', validators=[Optional()])

    smoking = SelectField(u'การสูบบุหรี่/ยาสูบ',
            choices=[('', u'โปรดเลือก'),
                ('no', u'ไม่เคยสูบเลย'),
                ('yes', u'ปัจจุบันยังสูบ'),
                ('quit', u'เคยสูบ (ตอนนี้เลิกแล้ว)'),
                ], default='', validators=[Optional()])

    smoke_freq = SelectField(u'ความถี่',
            choices=[('', u'โปรดเลือก'),
                ('sometimes', u'บ่อยครั้ง'),
                ('daily', u'ทุกวัน'),
                ], default='', validators=[Optional()])

    smoke_per_week = IntegerField(u'จำนวนมวนต่อสัปดาห์', validators=[Optional()])
    smoke_per_day = IntegerField(u'จำนวนมวนต่อวัน', validators=[Optional()])

    smoke_years = IntegerField(u'เป็นเวลา (ปี)', validators=[Optional()])
    quit_smoke_years = IntegerField(u'เลิกมา (ปี)', validators=[Optional()])

    alcohol = SelectField(u'ดื่มแอลกอฮอล์',
            choices=[('', u'โปรดเลือก'),
                ('no', u'ไม่เคยดื่ม'),
                ('sometimes', u'บางครั้ง'),
                ('daily', u'ทุกวัน'),
                ('quit', u'เคยดื่ม'),
                ], default='', validators=[Optional()])

    drink_per_day = IntegerField(u'จำนวนแก้ว (ต่อวัน)', validators=[Optional()])
    drink_years = IntegerField(u'เป็นเวลา (ปี)', validators=[Optional()])
    quit_drink_years = IntegerField(u'เลิกมา (ปี)', validators=[Optional()])

    congenital_disease = SelectField(u'โรคประจำตัว',
            choices=[('', u'โปรดเลือก'),
                (u'ไม่มีโรคประจำตัว', u'ไม่มีโรคประจำตัว'),
                (u'โรคเบาหวาน', u'โรคเบาหวาน'),
                (u'โรคความดันโลหิตสูง', u'โรคความดันโลหิตสูง'),
                (u'โรคหอบหืด', u'โรคหอบหืด'),
                (u'โรคไขมันในเลือดผิดปกติ', u'โรคไขมันในเลือดผิดปกติ'),
                (u'โรคหัวใจ', u'โรคหัวใจ'),
                (u'โรคมะเร็ง', u'โรคมะเร็ง'),
                (u'โรคปอดอุดกั้นเรื้อรัง', u'โรคปอดอุดกั้นเรื้อรัง'),
                (u'อื่นๆ', u'อื่นๆ'),
                ], default='', validators=[Optional()])

    congenital_dis_other = StringField(u'อื่นๆ โปรดระบุ', validators=[Optional()])
    congenital_dis_years = IntegerField(u'เป็นมาเป็นเวลา (ปี)', validators=[Optional()])

    # Other parts
    fpg_level = DecimalField(u'น้ำตาลในเลือด', validators=[Optional()])
    fcg_level = DecimalField(u'น้ำตาลปลายนิ้ว', validators=[Optional()])
    systolic = IntegerField(u'ความดันโลหิตตัวบน หรือซิสโตลิค (SBP)', validators=[Optional()])
    diastolic = IntegerField(u'ความดันโลหิตตัวล่าง หรือไดแอสโตลิค (DBP)', validators=[Optional()])
    smoke_screening = BooleanField(u'ยังคงสูบบุหรี่ ยาเส้น ยาสูบ บุหรี่ซิกาแรต บุหรี่ซิการ์ หรือหยุดสูบไม่เกิน 1 ปี', validators=[Optional()])
    bp = BooleanField(u'ระดับความดันโลหิต >=130/85 มม.ปรอท และ/หรือ เคยได้รับการวินิจฉัยจากแพทย์ว่าเป็นความดันโลหิตสูง', validators=[Optional()])
    fpg = BooleanField(u'ระดับน้ำตาลในเลือด (FPG) >=100 มก./ดล. และ/หรือ เคยได้รับการวินิจฉัยจากแพทย์ว่าเป็นโรคเบาหวาน', validators=[Optional()])
    abnormal_lipid = BooleanField(u'เคยได้รับการวินิจฉัยจากแพทย์ว่ามีภาวะไขมันเลือดผิดปกติโดย<br>TC >280 มก./ดล. และ/หรือ LDL >100 มก./ดล. และ/หรือ TG >150 มก./ดล. และ/หรือ ในชาย HDL <40 มก./ดล. ในหญิง HDL <50 มก./ดล.', validators=[Optional()])
    waist = BooleanField(u'เส้นรอบเอวมากกว่าส่วนสูง (ซม.) หาร 2', validators=[Optional()])
    infarction = BooleanField(u'เคยได้รับการวินิจฉัยจากแพทย์ว่าเป็นโรคหัวใจขาดเลือด หรืออัมพฤกษ์ อัมพาต', validators=[Optional()])
    family_infarction = BooleanField(u'มีญาติสายตรง (พ่อ แม่ พี่หรือน้องท้องเดียวกัน) ที่แพทย์วินิจฉัยว่าเป็นโรคหัวใจขาดเลือด หรืออัมพฤกษ์ อัมพาต (ผู้ชายเป็นก่อนอายุ 55 ปี ผู้หญิงเป็นก่อนอายุ 65 ปี)', validators=[Optional()])
    dental_brushing = SelectField(u'',
            choices=[('', u'โปรดเลือก'),
                (u'ไม่ได้แปรง/ไม่ได้ใช้แปรงสีฟัน', u'ไม่ได้แปรง/ไม่ได้ใช้แปรงสีฟัน'),
                (u'แปรงวันละ 1 ครั้ง ก่อนนอน', u'แปรงวันละ 1 ครั้ง ก่อนนอน'),
                (u'แปรงวันละ 2 ครั้ง เช้าและก่อนนอน', u'แปรงวันละ 2 ครั้ง เช้าและก่อนนอน'),
                (u'แปรงมากกว่าวันละ 2 ครั้ง', u'แปรงมากกว่าวันละ 2 ครั้ง'),
                (u'อื่นๆ', u'อื่นๆ'),
                ], default='', validators=[Optional()])
    dental_brushing_gt_twice = IntegerField(u'ระบุ', validators=[Optional()])
    dental_brushing_other = StringField(u'อื่นๆ โปรดระบุ', validators=[Optional()])

    fluoride_toothpaste = BooleanField(u'การใช้ยาสีฟันผสมฟลูโอไรด์ทุกวัน',
            validators=[Optional()])
    dental_floss = BooleanField(u'การทำความสะอาดซอกฟันทุกวัน', validators=[Optional()])
    dental_floss_equip = StringField(u'ใช้อุปกรณ์ได้แก่', validators=[Optional()])
    smoke_ten_cig = BooleanField(u'สูบบุหรี่มากกว่า 10 มวนต่อวัน', validators=[Optional()])
    chew_gum = BooleanField(u'เคี้ยวหมากเป็นประจำ', validators=[Optional()])

    dental_part_two_one = RadioField(u'<u>เนื้อเยื่อในช่องปาก</u><br>บริเวณริมฝีปาก แก้ม ลิ้น มีปุ่ม ก้อนเนื้อ มีแผลเรื้อรังหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int, validators=[Optional()])
    dental_part_two_two = RadioField(u'<u>เหงือกและอวัยวะปริทันต์</u><br>บริเวณเหงือกมีเลือดออก มีฝีหนอง ฟันโยกหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int, validators=[Optional()])
    dental_part_two_three = RadioField(u'<u>ฟันผุ</u><br>มีฟันผุเป็นรู เสียวฟัน ฟันหัก ฟันแตกเหลือแต่ตอฟันหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int, validators=[Optional()])
    dental_part_two_four = RadioField(u'<u>ปัญหาการเคี้ยวอาหาร/การกลืน</u><br>มีปัญหาการเคี้ยวอาหารการกลืนหรือไม่',
            choices=[(0, u'ปกติ'), (1, u'ผิดปกติ')], coerce=int, validators=[Optional()])
    dental_part_two_five = RadioField(u'<u>ฟันเทียม</u><br>จำเป็นต้องใส่ฟันเทียมหรือทำฟันเทียมหรือไม่',
            choices=[(1, u'จำเป็น'), (0, u'ไม่จำเป็น')], coerce=int, validators=[Optional()])
    dental_part_two_six = RadioField(u'<u>การได้รับการตรวจหรือรักษาจากทันตบุคลากร</u><br>ท่านเคยได้รับการตรวจหรือรักษาจากทันตบุคลากรหรือไม่',
            choices=[(0, u'เคย'), (1, u'ไม่เคย')], coerce=int, validators=[Optional()])
    dental_part_two_seven = RadioField(u'<u>ความต้องการการรักษาทางทันตกรรม</u><br>ปัจจุบันท่านต้องการการรักษาหรือไม่',
            choices=[(1, u'ต้องการ'), (0, u'ไม่ต้องการ')], coerce=int, validators=[Optional()])

    dental_part_two_one_follow_up = BooleanField(u'ใช่', validators=[Optional()])
    dental_part_two_two_follow_up = BooleanField(u'ใช่', validators=[Optional()])
    dental_part_two_three_follow_up = BooleanField(u'ใช่', validators=[Optional()])
    dental_part_two_four_follow_up = BooleanField(u'ใช่', validators=[Optional()])
    dental_part_two_five_follow_up = BooleanField(u'ใช่', validators=[Optional()])
    dental_part_two_six_follow_up = BooleanField(u'ใช่', validators=[Optional()])
    dental_part_two_seven_follow_up = BooleanField(u'ใช่', validators=[Optional()])

    dental_transfer_tissue = BooleanField(u'เนื้อเยื่อในช่องปาก', validators=[Optional()])
    dental_transfer_gum = BooleanField(u'เหงือกและอวัยวะปริทันต์', validators=[Optional()])
    dental_transfer_cavity = BooleanField(u'ฟันผุ', validators=[Optional()])
    dental_transfer_swallow = BooleanField(u'ปัญหาการเคี้ยวอาหาร/การกลืน', validators=[Optional()])
    dental_transfer_denture = BooleanField(u'ฟันเทียม', validators=[Optional()])

    eye_exam_one = BooleanField(u'นับนิ้วในระยะสามเมตรได้ถูกต้อง<u>น้อยกว่า 3 ใน 4 ครั้ง</u>', validators=[Optional()])
    eye_exam_two = BooleanField(u'อ่านหนังสือพิมพ์หน้าหนึ่งในระยะหนึ่งฟุต<u>ไม่ได้</u>', validators=[Optional()])
    eye_exam_three = BooleanField(u'ปิดตาดูทีละข้าง <u>พบว่า</u> ตามัวคล้ายมีหมอกบัง', validators=[Optional()])
    eye_exam_four = BooleanField(u'ปิดตาดูทีละข้าง <u>พบว่า</u> มองเห็นชัดแต่ตรงกลาง ไม่เห็นรอบข้าง หรือมักเดินชนประตู สิ่งของบ่อยๆ', validators=[Optional()])
    eye_exam_five = BooleanField(u'ปิดตาดูทีละข้าง <u>พบว่า</u> เห็นจุดดำกลางภาพ หรือเห็นภาพบิดเบี้ยว', validators=[Optional()])

    eye_exam_three_side = RadioField(u'', choices=[
        ('left', u'ซ้าย'),
        ('right', u'ขวา'),
        ], validators=[Optional()])
    eye_exam_four_side = RadioField(u'', choices=[
        ('left', u'ซ้าย'),
        ('right', u'ขวา'),
        ], validators=[Optional()])
    eye_exam_five_side = RadioField(u'', choices=[
        ('left', u'ซ้าย'),
        ('right', u'ขวา'),
        ], validators=[Optional()])

    snellen_left = SelectField(u'ตาซ้าย', choices=[
        (-1, u'โปรดเลือก'),
        (1, '20/200'),
        (2, '20/100'),
        (3, '20/70'),
        (4, '20/50'),
        (5, '20/40'),
        (6, '20/30'),
        (7, '20/20'),
        ], default=None, coerce=int, validators=[Optional()])

    snellen_right = SelectField(u'ตาขวา', choices=[
        (-1, u'โปรดเลือก'),
        (1, '20/200'),
        (2, '20/100'),
        (3, '20/70'),
        (4, '20/50'),
        (5, '20/40'),
        (6, '20/30'),
        (7, '20/20'),
        ], default=None, coerce=int, validators=[Optional()])

    amt_one = BooleanField(u'อายุเท่าไหร่', validators=[Optional()])
    amt_two = BooleanField(u'ขณะนี้เวลาอะไร', validators=[Optional()])
    amt_three = BooleanField(u'ที่อยู่ปัจจุบันของท่านคือ', validators=[Optional()])
    amt_four = BooleanField(u'ปีนี้ปีอะไร', validators=[Optional()])
    amt_five = BooleanField(u'สถานที่ตรงนี้เรียกว่าอะไร', validators=[Optional()])
    amt_six = BooleanField(u'คนนี้คือใคร (ชี้ที่คนสัมภาษณ์) และคนนี้คือใคร (ชี้ที่คนข้างๆ : ญาติ)', validators=[Optional()])
    amt_seven = BooleanField(u'วันเดือนปีเกิดของท่านคือ', validators=[Optional()])
    amt_eight = BooleanField(u'เหตุการณ์ 14 ตุลา หรือเหตุการณ์มหาวิปโยคเกิดขึ้นในปีพ.ศ.อะไร', validators=[Optional()])
    amt_nine = BooleanField(u'พระมหากษัตริย์องค์ปัจจุบันมีพระนามว่าอะไร', validators=[Optional()])
    amt_ten = BooleanField(u'ให้นับถอยหลังจาก 20 ถึง 1', validators=[Optional()])

    mmse_one_one = RadioField(u'วันนี้ วันที่เท่าไหร่', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_one_two = RadioField(u'วันนี้ วันอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_one_three = RadioField(u'เดือนนี้ เดือนอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_one_four = RadioField(u'ปีนี้ ปีอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_one_five = RadioField(u'ฤดูนี้ ฤดูอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_one_one = RadioField(u'สถานที่ตรงนี้เรียกว่าอะไรและชื่อว่าอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_one_two = RadioField(u'ขณะนี้อยู่ชั้นที่เท่าไหร่ของตัวอาคาร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_one_three = RadioField(u'ที่นี่อยู่ในอำเภออะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_one_four = RadioField(u'ที่นี่จังหวัดอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_one_five = RadioField(u'ที่นี่ภาคอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])

    mmse_two_two_one = RadioField(u'สถานที่ตรงนี้เรียกว่าอะไร และเลขที่เท่าไหร่', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_two_two = RadioField(u'ที่นี่หมู่บ้าน (หรือละแวก คุ้ม ย่าน ถนน) อะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_two_three = RadioField(u'ที่นี่อำเภอ หรือเขตอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_two_four = RadioField(u'ที่นี่จังหวัดอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_two_two_five = RadioField(u'ที่นี่ภาคอะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])

    mmse_three_flower = BooleanField(u'ดอกไม้', validators=[Optional()])
    mmse_three_river = BooleanField(u'แม่น้ำ', validators=[Optional()])
    mmse_three_train = BooleanField(u'รถไฟ', validators=[Optional()])
    mmse_three_tree = BooleanField(u'ต้นไม้', validators=[Optional()])
    mmse_three_sea = BooleanField(u'ทะเล', validators=[Optional()])
    mmse_three_car = BooleanField(u'รถยนต์', validators=[Optional()])

    mmse_four_one = RadioField(u'คิดเลขในใจโดยให้เอา 100 ตั้งลบออกทีละ 7 ไปเรื่อยๆ', choices=[
        (1, u'1 คะแนน'),
        (2, u'2 คะแนน'),
        (3, u'3 คะแนน'),
        (4, u'4 คะแนน'),
        (5, u'5 คะแนน'),
        (6, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])

    mmse_four_two = RadioField(u'สะกดคำว่ามะนาวถอยหลัง', choices=[
        (1, u'1 คะแนน'),
        (2, u'2 คะแนน'),
        (3, u'3 คะแนน'),
        (4, u'4 คะแนน'),
        (5, u'5 คะแนน'),
        (6, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])

    mmse_five_flower = BooleanField(u'ดอกไม้', validators=[Optional()])
    mmse_five_river = BooleanField(u'แม่น้ำ', validators=[Optional()])
    mmse_five_train = BooleanField(u'รถไฟ', validators=[Optional()])
    mmse_five_tree = BooleanField(u'ต้นไม้', validators=[Optional()])
    mmse_five_sea = BooleanField(u'ทะเล', validators=[Optional()])
    mmse_five_car = BooleanField(u'รถยนต์', validators=[Optional()])

    mmse_six_one = RadioField(u'ยื่นดินสอให้ผู้ถูกทดสอบดูแล้วถามว่า สิ่งนี้คืออะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])
    mmse_six_two = RadioField(u'ชี้นาฬิกาข้อมือให้ผู้ถูกทดสอบดูแล้วถามว่านี่คืออะไร', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])

    mmse_seven_one = RadioField(u'พูดตามคำว่า "ใครใคร่ขายไข่ไก่"', choices=[
        (1, u'ถูกต้อง'),
        (2, u'ผิด'),
        (0, u'ไม่ได้ทำ'),
        ], coerce=int, validators=[Optional()])

    mmse_eight_one = BooleanField(u'รับด้วยมือขวา', validators=[Optional()])
    mmse_eight_two = BooleanField(u'พับครึ่งด้วยมือสองข้าง', validators=[Optional()])
    mmse_eight_three = BooleanField(u'วางไว้ที่ (พื้น โต๊ะ เตียง)', validators=[Optional()])

    mmse_nine_one = BooleanField(u'หลับตาได้', validators=[Optional()])
    mmse_ten_one = BooleanField(u'ประโยคมีความหมาย', validators=[Optional()])
    mmse_eleven_one = BooleanField(u'วาดได้', validators=[Optional()])

    q2_one = BooleanField(u'<u>ใน 2 สับดาห์ที่ผ่านมาท่านรู้สึก</u> หดหู่ หรือ ท้อแท้ สิ้นหวังหรือไม่', validators=[Optional()])
    q2_two = BooleanField(u'<u>ใน 2 สับดาห์ที่ผ่านมาท่านรู้สึก</u> เบื่อ ทำอะไรก็ไม่เพลิดเพลินหรือไม่', validators=[Optional()])

    q9_choices = [(-1, u'โปรดเลือก'),
                    (0, u'ไม่มีเลย'),
                    (1, u'เป็นบางวัน (1-7 วัน)'),
                    (2, u'เป็นบ่อย (>7 วัน)'),
                    (3, u'เป็นทุกวัน')]
    q9_one = SelectField(u'เบื่อ ไม่สนใจไม่อยากทำอะไร',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_two = SelectField(u'ไม่สบายใจ ซึมเศร้า ท้อแท้',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_three = SelectField(u'หลับยาก หรือหลับๆ ตื่นๆ หรือหลับมากไป',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_four = SelectField(u'เหนื่อยง่าย หรือไม่ค่อยมีแรง',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_five = SelectField(u'เบื่ออาหาร หรือกินมากเกินไป',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_six = SelectField(u'รู้สึกไม่ดีกับตัวเอง คิดว่าตัวเองล้มเหลว หรือทำให้ตัวเองหรือครอบครัวผิดหวัง',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_seven = SelectField(u'สมาธิไม่ดีเวลาทำอะไร เช่น ดูโทรทัศน์ ฟังวิทยุ หรือทำงานที่ต้องใช้ความตั้งใจ',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_eight = SelectField(u'พูดช้า ทำอะไรช้าลงจนคนอื่นสังเกตเห็นได้ หรือกระสับกระส่ายไม่สามารถอยู่นิ่งได้เหมือนที่เคยเป็น',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])
    q9_nine = SelectField(u'คิดทำร้ายตนเอง หรือคิดว่าถ้าตายไปคงจะดี',
        choices=q9_choices, default=None, coerce=int, validators=[Optional()])

    knee_pain = RadioField(u'ผู้สูงอายุมีอาการปวดเข่า',
            choices=[(0, u'ไม่ปวดเข่า'), (1, u'ปวดเข่า')], coerce=int, validators=[Optional()])

    knee_pain_clinic_one = BooleanField(u'ข้อเข่าฝืดตึงหลังตื่นนอนตอนเช้านาน <30 นาที (stiffness)', validators=[Optional()])
    knee_pain_clinic_two = BooleanField(u'เสียงดังกรอบแกรบในข้อเข่าขณะเคลื่นไหว (crepitus)', validators=[Optional()])
    knee_pain_clinic_three = BooleanField(u'กดเจ็บที่กระดูข้อเข่า (bony tenderness)', validators=[Optional()])
    knee_pain_clinic_four = BooleanField(u'ข้อใหญ่ผิดรูป (bony enlargement)', validators=[Optional()])
    knee_pain_clinic_five = BooleanField(u'ไม่พบข้ออุ่น (no palpable warmth)', validators=[Optional()])

    tugt = RadioField(u'', choices=[
        (0, u'<30 วินาที'),
        (1, u'>=30 วินาที'),
        (2, u'เดินไม่ได้'),
        ], coerce=int, validators=[Optional()])

    urine_holding = RadioField(u'ผู้สูงอายุมีภาวะ <u>"ปัสสาวะเล็ด"</u> หรือ <u>"ปัสสาวะราด"</u> จนทำให้เกิดปัญหาในการใช้ชีวิตประจำวัน',
                        choices=[(0, u'ไม่มี'), (1, u'มี')], coerce=int, validators=[Optional()])

    bmi = SelectField(u'ค่า BMI ', choices=[
        (-1, u'โปรดเลือก'),
        (1, '<18.5'),
        (2, '18.5-22.9'),
        (3, '23.0-24.9'),
        (4, '25.0-29.9'),
        (5, '>=30'),
        (0, u'ไม่ระบุ'),
        ], default=None, coerce=int, validators=[Optional()])

    malnutrition_one = RadioField(u'ในช่วงเวลาที่ผ่านมารับประทานอาหารได้น้อยลง เนื่องจากความอยากอาหารลดลง มีปัญหาการย่อย การเคี้ยวหรือการกลืน หรือไม่',
                            choices=[(0,u'ความอยากอาหารลดลงอย่างมาก'), (1, u'ความอยากอาหารลดลงปานกลาง'),
                                        (2, u'ความอยากอาหารไม่ลดลง')], coerce=int, validators=[Optional()])
    malnutrition_two = RadioField(u'ในช่วงสามเดือนที่ผ่านมา น้ำหนักลดลงหรือไม่',
                            choices=[(0, u'ลดมากกว่า 3 กิโลกรัม'), (1, u'ไม่ทราบ'),
                                        (2, u'น้ำหนักลดลงระหว่าง 1-3 กิโลกรัม'), (3, u'น้ำหนักไม่ลดลง')],
                            coerce=int, validators=[Optional()])
    malnutrition_three = RadioField(u'เคลื่อนไหวได้เองหรือไม่',
                            choices=[(0, u'นอนบนเตียงต้องอาศัยรถเข็นตลอดเวลา'),
                                        (1, u'ลุกจากเตียงหรือรถเข็นได้บ้าง แต่ไม่สามารถไปข้างนอกได้เอง'),
                                        (2, u'เดินและเคลื่อนไหวได้ปกติ')], coerce=int, validators=[Optional()])
    malnutrition_four = RadioField(u'ในสามเดือนที่ผ่านมามีความเครียดรุนแรงหรือป่วยเฉียบพลันหรือไม่',
                            choices=[(0, u'มี'), (2, u'ไม่มี')], coerce=int, validators=[Optional()])
    malnutrition_five = RadioField(u'มีปัญหาทางจิตประสาทหรืิอไม่',
                            choices=[(0,u'ความจำเสื่อมหรือซึมเศร้าอย่างรุนแรง'),
                                        (1, u'ความจำเสื่อมเล็กน้อย'),
                                        (2, u'ไม่มีปัญหาทางจิตประสาท')],
                            coerce=int, validators=[Optional()])
    malnutrition_six = RadioField(u'ดัชนีมวลกาย',
                            choices=[(0, u'BMI น้อยกว่า 19'), (1, u'BMI ตั้งแต่ 19 แต่น้อยกว่า 21'),
                                        (2, u'BMI ตั้งแต่ 21 แต่น้อยกว่า 23'), (3, u'BMI มากกว่า 23')],
                            coerce=int, validators=[Optional()])

    sleeping_one = RadioField(u'ผู้สูงอายุมีปัญหาในการนอนหรือไม่',
                        choices=[(0, u'ไม่มีปัญหา'), (1, u'มีปัญหา')],
                        coerce=int, validators=[Optional()])
    insomnia = BooleanField(u'นอนไม่หลับ', validators=[Optional()])
    oversleep = BooleanField(u'นอนมากไป', validators=[Optional()])
    snore = BooleanField(u'นอนกรน', validators=[Optional()])
    dreamwalk = BooleanField(u'นอนละเมอ', validators=[Optional()])
    sleeping_other = StringField(u'อื่นๆ โปรดระบุ', validators=[Optional()])
    sleeping_period_year = IntegerField(u"ระยะเวลาที่มีปัญหาในการนนอนหลับ ปี", validators=[Optional()])
    sleeping_period_month = IntegerField(u"เดือน", validators=[Optional()])
    sleeping_avg_hours = IntegerField(u'โดยเฉลี่ยผู้สูงอายุได้นอนหลับคืนละ', validators=[Optional()])
    fatique = BooleanField(u'ผู้สูงอายุมีอาการอ่อนเพลียตอนกลางวันหรือไม่', validators=[Optional()])

    routine_one = RadioField(u'Feeding (รับประทานอาหารเมื่อเตรียมสำรับไว้ล่วงหน้า)', choices=[
        (0, u'ไม่สามารถตักอาหารเข้าปากได้ ต้องมีคนป้อนให้'),
        (1, u'ตักอาหารเองได้แต่ต้องมีคนช่วย เช้น ช่วยใช้ช้อนตักเตรียมไว้ให้หรือตัดเป็นเล็กๆไว้ล่วงหน้า'),
        (2, u'ตักอาหารและช่วยตัวเองได้เป็นปกติ')
        ], coerce=int, validators=[Optional()])

    routine_two = RadioField(u'Grooming (ล้างหน้า หวีผม แปรงฟัน โกนหนวดในระยะเวลา 24-48 ชม.ที่ผ่านมา)',
            choices=[
                (0, u'ต้องการความช่วยเหลือ'),
                (1, u'ทำเองได้ หรือทำเองได้ถ้าเตรียมอุปกรณ์ไว้ให้')
                ], coerce=int, validators=[Optional()])

    routine_three = RadioField(u'Transfer (ลุกจากที่นอนหรือเตียงไปที่เก้าอี้)',
            choices=[
                (0, u'ไม่สามารถนั่งได้ นั่งแล้วจะล่มเสมอ หรือต้องใช้สองคนช่วยกันยกขึ้น'),
                (1, u'ต้องการความช่วยเหลืออย่างมากจึงจะนั่งได้เช่นต้องใช้คนที่แข็งแรงหรือมีทักษะ 1 คน หรือใช้คนทั่วไป 2 คนพยุง'),
                (2, u'ต้องการความช่วยเหลือบ้างเช่น บอกให้ทำตาม หรือช่วยพยุงเล็กน้อยหรือต้องมีคนดูแลเพื่อความปลอดภัย')
                ], coerce=int, validators=[Optional()])

    routine_four = RadioField(u'Toilet use (ใช้ห้องน้ำ)',
            choices=[
                (0, u'ช่วยตัวเองไม่ได้'),
                (1, u'ทำเองได้บ้าง (อย่างน้อยทำความสะอาดตัวเองได้หลังเสร็จธุระ) แต่ต้องการความช่วยเหลือในบางสื่ง'),
                (2, u'ช่วยตัวเองได้ดี (ขึ้นนั่งและลงจากโถส้วมเองได้ ทำความสะอาดได้เรียบร้อยหลังเสร็จธุระ ถอดใส่เสื้อผ้าได้เรียบร้อย)')
                ], coerce=int, validators=[Optional()])

    routine_five = RadioField(u'Mobility (การเคลื่อนที่ภายในห้องหรือบ้าน)',
            choices=[
                (0, u'เคลื่อนที่ไปไหนไม่ได้'),
                (1, u'ต้องใช้รถเข็นช่วยตัวเองให้เคลื่อนที่ได้เอง (ไม่ต้องมีคนเข็นให้) และเข้าออกมุมห้องหรือประตูได้'),
                (2, u'เดินหรือเคลื่อนที่โดยมีตนช่วย เช้น พยุง หรือบอกให้ทำตาม หรือต้องให้ความสนใจ ดูแลเพื่อความปลอดภัย'),
                (3, u'เดินหรือเคลื่อนที่ได้เอง')
                ], coerce=int, validators=[Optional()])

    routine_six = RadioField(u'Dressing (การสวมใส่เสื้อผ้า)',
            choices=[
                (0, u'ต้องมีคนสวมใส่ให้ ช่วยต้วเองแทบไม่ได้หรือได้น้อย'),
                (1, u'ช่วยตัวเองได้ประมาณร้อยละ 50 ที่เหลือต้องมีคนช่วย'),
                (2, u'ช่วยตัวเองได้ดี (รวมทั้งการติดกระดุม รูดซิบ หรือใช้เสื้อผ้าที่ดัดแปลงให้เหมาะสมก็ได้)')
                ], coerce=int, validators=[Optional()])

    routine_seven = RadioField(u'Stairs (การขึ้นลงบันได 1 ขั้น)',
            choices=[
                (0, u'ไม่สามารถทำได้'),
                (1, u'ต้องการคนช่วย'),
                (2, u'ขึ้นลงเองได้ (ถ้าต้องใช้เครื่องช่วยเดิน เช่น walker จะต้องเอาขึ้นลงได้ด้วย)')
                ], coerce=int, validators=[Optional()])

    routine_eight = RadioField(u'Bathing (การอาบน้ำ)',
            choices=[
                (0, u'ต้องมีคนด้วยหรือทำให้'),
                (1, u'อาบเองได้')
                ], coerce=int, validators=[Optional()])

    routine_nine = RadioField(u'Bowels (การกลั้นการถ่ายอุจจาระในระยะ 1 สัปดาห์ที่ผ่านมา)',
            choices=[
                (0, u'กลั้นไม่ได้ หรือต้องการการสวนอุจจาระอยู่เสมอ'),
                (1, u'กลั้นไม่ได้บางครั้ง (เป็นน้อยกว่า 1 ครั้งต่อสัปดาห์)'),
                (2, u'กลั้นได้ปกติ')
                ], coerce=int, validators=[Optional()])

    routine_ten = RadioField(u'Bladder (การกลั้นปัสสาวะในระยะ 1 สัปดาห์ที่ผ่านมา)',
            choices=[
                (0, u'กลั้นไม่ได้ หรือต้องการการสวนอุจจาระอยู่เสมอ'),
                (1, u'กลั้นไม่ได้บางครั้ง (เป็นน้อยกว่า 1 ครั้งต่อสัปดาห์)'),
                (2, u'กลั้นได้ปกติ')
                ], coerce=int, validators=[Optional()])

    long_term_care_one_one = RadioField(u'การอยู่อาศัย หรือผู้ดูแลเมื่อเจ็บป่วย',
            choices=[
                (0, u'ไม่ได้อยู่คนเดียว หรือ มีคนดูแลเมื่อเจ็บป่วย'),
                (1, u'อยู่คนเดียว หรือไม่มีคนดูแลเมื่อเจ็บป่วย')
                ], coerce=int, validators=[Optional()])

    long_term_care_one_two = RadioField(u'ลักษณะที่อยู่อาศัย',
            choices=[
                (0, u'มั่นคงแข็งแรง หรือไม่มั่นคงแต่ไม่มีผลต่อความปลอดภัยในชีวิตและสุขภาพ'),
                (1, u'ไม่มีที่อยู่อาศัยหรือมีที่อยู่อาศัยแต่ไม่ปลอดภัยต่อสุขภาพ')
                ], coerce=int, validators=[Optional()])

    long_term_care_one_three = RadioField(u'ความเพียงพอของรายได้ในการดำเนินชีวิตประจำวัน',
            choices=[
                (0, u'เพียงพอ'),
                (1, u'ไม่เพียงพอ')
                ], coerce=int, validators=[Optional()])

    long_term_care_two_one = RadioField(u'ความสามารถในการมองเห็น',
            choices=[
                (0, u'ชัดเจนโดยไม่ต้องใส่แว่น'),
                (1, u'ชัดเจนแต่ต้องใส่แว่น'),
                (2, u'ไม่ชัดเจนแต่ไม่มีปัญหาในการทำชีวิตประจำวัน'),
                (3, u'ไม่ชัดเจนและมีปัญหาในการทำกิจกรรมประจำวัน'),
                (4, u'ไม่เห็นเลย'),
                ], coerce=int, validators=[Optional()])

    long_term_care_two_two = RadioField(u'ชัดเจนโดยไม่ต้องใข้เครื่องช่วย',
            choices=[
                (0, u'ชัดเจนโดยไม่ต้องใช้เครื่องช่วยฟัง'),
                (1, u'ชัดเจนแต่ไม่ต้องใช้เครื่องช่วยฟัง'),
                (2, u'ไม่ชัดเจนแต่ไม่มีปัญหาในการทำชีวิตประจำวัน'),
                (3, u'ไม่ชัดเจนและมีปัญหาในการทำกิจกรรมประจำวัน'),
                (4, u'ไม่ได้ยินเลย'),
                ], coerce=int, validators=[Optional()])

    long_term_care_three_one = RadioField(u'มีอาการหลงลืม/ลืมเหตุการณ์ที่เพิ่งเกิดขึ้น เช่นกินข้าวแล้วบอกยังไม่ได้กิน',
            choices=[
                (0, u'ไม่มี'),
                (1, u'มี')
                ], coerce=int, validators=[Optional()])

    long_term_care_three_two_one = BooleanField(u'หดหู่เศร้า หรือท้อแท้สิ้นหวัง', validators=[Optional()])
    long_term_care_three_two_two = BooleanField(u'เบื่อทำอะไรก็ไม่เพลิน', validators=[Optional()])

    long_term_care_four_one = BooleanField(u'ใน 1 ปีที่ผ่านมาน้ำหนักลดลงมากกว่า  1 กิโลกรัม', validators=[Optional()])
    long_term_care_four_two = BooleanField(u'ท่านรู้สึกเหนื่อยตลอดเวลา', validators=[Optional()])
    long_term_care_four_three = BooleanField(u'ท่านไม่สามารถเดินได้โดยลำพังต้องมีคนช่วยพยุง', validators=[Optional()])
    long_term_care_four_four = BooleanField(u'ใช้เวลา 7 นาทีขึ้นไป หรือไม่สามารถเดินได้', validators=[Optional()])
    long_term_care_four_five = BooleanField(u'ผู้สูงอายุมีความอ่อนแรงของกำลังมือและแขน ขา ชัดเจน', validators=[Optional()])

    long_term_care_five_choices = [(0, u'ทำได้ด้วยตัวเองรวมใช้อุปกรณ์ช่วย'),
                                (1, u'ทำด้วยตัวเองได้บ้าง ต้องมีคนช่วยจึงทำได้สำเร็จ'),
                                (2, u'ทำด้วยตนเองไม่ได้เลย')]
    long_term_care_five_one = RadioField(u'ลุกจากที่นอนหรือเตียง',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])

    long_term_care_five_two = RadioField(u'ล้างหน้า แปรงฟัน หวีผม',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_three = RadioField(u'อาบน้ำ',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_four = RadioField(u'สวมใส่เสื้อผ้า',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_five = RadioField(u'ตักหรือหยิบอาหารทาน',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_six = RadioField(u'การใช้ห้องส้วมและทำความสะอาดหลังขับถ่าย',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_seven = RadioField(u'เดินหรือเคลื่อนที่ภายในบ้าน', choices=long_term_care_five_choices, coerce=int, validators=[Optional()])
    long_term_care_five_eight = RadioField(u'ขึ้นลงบันได 1 ชั้น',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_nine = RadioField(u'กลั้นปัสสาวะ',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_ten = RadioField(u'กลั้นอุจจาระ',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_eleven = RadioField(u'เดินหรือเคลื่อนที่ออกจากบ้าน',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_twelve = RadioField(u'ทำหรือเตรียมอาหาร',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_thirteen = RadioField(u'กวาด/ถูบ้านซักรีดผ้า',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_fourteen = RadioField(u'การซื้อของ จ่ายตลาด',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_fifteen = RadioField(u'ใช้บริการระบบสาธารณะ เช่น รถโดยสาร รถเมล์ แท็กซี่ รถไฟ',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])
    long_term_care_five_sixteen = RadioField(u'การรับประทานยาตามแพทย์สั่ง',
                    choices=long_term_care_five_choices,
                    coerce=int, validators=[Optional()])

    submit = SubmitField('Submit')
