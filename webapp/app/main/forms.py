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

    snellen_left = SelectField(u'ตาซ้าย', choices=[
        ('20/200', '20/200'),
        ('20/100', '20/100'),
        ('20/70', '20/70'),
        ('20/50', '20/50'),
        ('20/40', '20/40'),
        ('20/30', '20/30'),
        ('20/20', '20/20'),
        ])

    snellen_right = SelectField(u'ตาขวา', choices=[
        ('20/200', '20/200'),
        ('20/100', '20/100'),
        ('20/70', '20/70'),
        ('20/50', '20/50'),
        ('20/40', '20/40'),
        ('20/30', '20/30'),
        ('20/20', '20/20'),
        ])

    amt_one = BooleanField(u'อายุเท่าไหร่')
    amt_two = BooleanField(u'ขณะนี้เวลาอะไร')
    amt_three = BooleanField(u'ที่อยู่ปัจจุบันของท่านคือ')
    amt_four = BooleanField(u'ปีนี้ปีอะไร')
    amt_five = BooleanField(u'สถานที่ตรงนี้เรียกว่าอะไร')
    amt_six = BooleanField(u'คนนี้คือใคร (ชี้ที่คนสัมภาษณ์) และคนนี้คือใคร (ชี้ที่คนข้างๆ :ญาติ)')
    amt_seven = BooleanField(u'วันเดือนปีเกิดของท่านคือ')
    amt_eight = BooleanField(u'เหตุการณ์ 14 ตุลา หรือเหตุการณ์มหาวิปโยคเกิดขึ้นในปีพ.ศ.อะไร')
    amt_nine = BooleanField(u'พระมหากษัตริย์องค์ปัจจุบันมีพระนามว่าอะไร')
    amt_ten = BooleanField(u'ให้นับถอยหลังจาก 20 ถึง 1')

    mmse_one_one = RadioField(u'วันนี้ วันที่เท่าไหร่', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_one_two = RadioField(u'วันนี้ วันอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_one_three = RadioField(u'เดือนนี้ เดือนอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_one_four = RadioField(u'ปีนี้ ปีอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_one_five = RadioField(u'ฤดูนี้ ฤดูอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_two_one_one = RadioField(u'สถานที่ตรงนี้เรียกว่าอะไรและชื่อว่าอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_one_two = RadioField(u'ขณะนี้อยู่ชั้นที่เท่าไหร่ของตัวอาคาร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_one_three = RadioField(u'ที่นี่อยู่ในอำเภออะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_one_four = RadioField(u'ที่นี่จังหวัดอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_one_five = RadioField(u'ที่นี่ภาคอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_two_two_one = RadioField(u'สถานที่ตรงนี้เรียกว่าอะไร และเลขที่เท่าไหร่', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_two_two = RadioField(u'ที่นี่หมู่บ้าน (หรือละแวก คุ้ม ย่าน ถนน) อะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_two_three = RadioField(u'ที่นี่อำเภอ หรือเขตอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_two_four = RadioField(u'ที่นี่จังหวัดอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_two_two_five = RadioField(u'ที่นี่ภาคอะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_three_flower = BooleanField(u'ดอกไม้')
    mmse_three_river = BooleanField(u'แม่น้ำ')
    mmse_three_train = BooleanField(u'รถไฟ')
    mmse_three_tree = BooleanField(u'ต้นไม้')
    mmse_three_sea = BooleanField(u'ทะเล')
    mmse_three_car = BooleanField(u'รถยนต์')

    mmse_four_one = RadioField(u'คิดเลขในใจโดยให้เอา 100 ตั้งลบออกทีละ 7 ไปเรื่อยๆ', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_four_two = RadioField(u'สะกดคำว่ามะนาวถอยหลัง', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_five_flower = BooleanField(u'ดอกไม้')
    mmse_five_river = BooleanField(u'แม่น้ำ')
    mmse_five_train = BooleanField(u'รถไฟ')
    mmse_five_tree = BooleanField(u'ต้นไม้')
    mmse_five_sea = BooleanField(u'ทะเล')
    mmse_five_car = BooleanField(u'รถยนต์')

    mmse_six_one = RadioField(u'ยื่นดินสอให้ผู้ถูกทดสอบดูแล้วถามว่า สิ่งนี้คืออะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])
    mmse_six_two = RadioField(u'ชี้นาฬิกาข้อมือให้ผู้ถูกทดสอบดูแล้วถามว่านี่คืออะไร', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_seven_one = RadioField(u'พูดตามคำว่า "ใครใคร่ขายไข่ไก่"', choices=[
        ('correct', u'ถูกต้อง'),
        ('wrong', u'ผิด'),
        ('na', u'ไม่ได้ทำ'),
        ])

    mmse_eight_one = BooleanField(u'รับด้วยมือขวา')
    mmse_eight_two = BooleanField(u'พับครึ่งด้วยมือสองข้าง')
    mmse_eight_three = BooleanField(u'วางไว้ที่ (พื้น โต๊ะ เตียง)')

    mmse_nine_one = BooleanField(u'หลับตาได้')
    mmse_ten_one = BooleanField(u'ประโยคมีความหมาย')
    mmse_eleven_one = BooleanField(u'วาดได้')

    q2_one = BooleanField(u'<u>ใน 2 สับดาห์ที่ผ่านมาท่านรู้สึก</u> หดหู่ หรือ ท้อแท้ สิ้นหวังหรือไม่')
    q2_two = BooleanField(u'<u>ใน 2 สับดาห์ที่ผ่านมาท่านรู้สึก</u> เบื่อ ทำอะไรก็ไม่เพลิดเพลินหรือไม่')

    q9_one = SelectField(u'เบื่อ ไม่สนใจไม่อยากทำอะไร', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_two = SelectField(u'ไม่สบายใจ ซึมเศร้า ท้อแท้', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_three = SelectField(u'หลับยาก หรือหลับๆ ตื่นๆ หรือหลับมากไป', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_four = SelectField(u'เหนื่อยง่าย หรือไม่ค่อยมีแรง', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_five = SelectField(u'เบื่ออาหาร หรือกินมากเกินไป', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_six = SelectField(u'รู้สึกไม่ดีกับตัวเอง คิดว่าตัวเองล้มเหลว หรือทำให้ตัวเองหรือครอบครัวผิดหวัง', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_seven = SelectField(u'สมาธิไม่ดีเวลาทำอะไร เช่น ดูโทรทัศน์ ฟังวิทยุ หรือทำงานที่ต้องใช้ความตั้งใจ', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_eight = SelectField(u'พูดช้า ทำอะไรช้าลงจนคนอื่นสังเกตเห็นได้ หรือกระสับกระส่ายไม่สามารถอยู่นิ่งได้เหมือนที่เคยเป็น', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])
    q9_nine = SelectField(u'คิดทำร้ายตนเอง หรือคิดว่าถ้าตายไปคงจะดี', choices=[
        (0, u'ไม่มีเลย'),
        (1, u'เป็นบางวัน (1-7 วัน)'),
        (2, u'เป็นบ่อย (>7 วัน)'),
        (3, u'เป็นุกวัน'),
        ])

    knee_pain = RadioField(u'ผู้สูงอายุมีอาการปวดเข่า',
            choices=[(False, u'ไม่ปวดเข่า'), (True, u'ปวดเข่า')])

    knee_pain_clinic_one = BooleanField(u'ข้อเข่าฝืดตึงหลังตื่นนอนตอนเช้านาน <30 นาที (stiffness)')
    knee_pain_clinic_two = BooleanField(u'เสียงดังกรอบแกรบในข้อเข่าขณะเคลื่นไหว (crepitus)')
    knee_pain_clinic_three = BooleanField(u'กดเจ็บที่กระดูข้อเข่า (bony tenderness)')
    knee_pain_clinic_four = BooleanField(u'ข้อใหญ่ผิดรูป (bony enlargement)')
    knee_pain_clinic_five = BooleanField(u'ไม่พบข้ออุ่น (no palpable warmth)')

    tugt = RadioField(u'', choices=[
        ('<30s', u'<30 วินาที'),
        ('>=30s', u'>=30 วินาที'),
        ('fail', u'เดินไม่ได้'),
        ])

    urine_holding = RadioField(u'ผู้สูงอายุมีภาวะ <u>"ปัสสาวะเล็ด"</u> หรือ <u>"ปัสสาวะราด"</u> จนทำให้เกิดปัญหาในการใช้ชีวิตประจำวัน',
                        choices=[(False, u'ไม่มี'), (True, u'มี')])

    bmi = SelectField(u'ค่า BMI ', choices=[
        ('<18.5', '<18.5'),
        ('18.5-22.9', '18.5-22.9'),
        ('23.0-24.9', '23.0-24.9'),
        ('25.0-29.9', '25.0-29.9'),
        ('>=30', '>=30'),
        ])

    malnutrition_one = RadioField(u'ในช่วงเวลาที่ผ่านมารับประทานอาหารได้น้อยลง เนื่องจากความอยากอาหารลดลง มีปัญหาการย่อย การเคี้ยวหรือการกลืน หรือไม่',
                            choices=[(0,u'ความอยากอาหารลดลงอย่างมาก'), (1, u'ความอยากอาหารลดลงปานกลาง'),
                                        (2, u'ความอยากอาหารไม่ลดลง')])
    malnutrition_two = RadioField(u'ในช่วงสามเดือนที่ผ่านมา น้ำหนักลดลงหรือไม่',
                            choices=[(0, u'ลดมากกว่า 3 กิโลกรัม'), (1, u'ไม่ทราบ'),
                                        (2, u'น้ำหนักลดลงระหว่าง 1-3 กิโลกรัม'), (3, u'น้ำหนักไม่ลดลง')])
    malnutrition_three = RadioField(u'เคลื่อนไหวได้เองหรือไม่',
                            choices=[(0, u'นอนบนเตียงต้องอาศัยรถเข็นตลอดเวลา'),
                                        (1, u'ลุกจากเตียงหรือรถเข็นได้บ้าง แต่ไม่สามารถไปข้างนอกได้เอง'),
                                        (2, u'เดินและเคลื่อนไหวได้ปกติ')])
    malnutrition_four = RadioField(u'ในสามเดือนที่ผ่านมามีความเครียดรุนแรงหรือป่วยเฉียบพลันหรือไม่',
                            choices=[(0, u'มี'), (1, u'ไม่มี')])
    malnutrition_five = RadioField(u'มีปัญหาทางจิตประสาทหรืิอไม่',
                            choices=[(0,u'ความจำเสื่อมหรือซึมเศร้าอย่างรุนแรง'),
                                        (1, u'ความจำเสื่อมเล็กน้อย'),
                                        (2, u'ไม่มีปัญหาทางจิตประสาท')])
    malnutrition_six = RadioField(u'ดัชนีมวลกาย',
                            choices=[(0, u'BMI น้อยกว่า 19'), (1, u'BMI ตั้งแต่ 19 แต่น้อยกว่า 21'),
                                        (2, u'BMI ตั้งแต่ 21 แต่น้อยกว่า 23'), (3, u'BMI มากกว่า 23')])

    sleeping_one = RadioField(u'ผู้สูงอายุมีปัญหาในการนอนหรือไม่',
                        choices=[(False, u'ไม่มีปัญหา'), (True, u'มีปัญหา')])
    insomnia = BooleanField(u'นอนไม่หลับ')
    oversleep = BooleanField(u'นอนมากไป')
    snore = BooleanField(u'นอนกรน')
    dreamwalk = BooleanField(u'นอนละเมอ')
    sleeping_other = StringField(u'อื่นๆ โปรดระบุ')
    sleeping_period_year = IntegerField()
    sleeping_period_month = IntegerField()
    sleeping_avg_hours = IntegerField(u'โดยเฉลี่ยผู้สูงอายุได้นอนหลับคืนละ')
    fatique = BooleanField(u'ผู้สูงอายุมีอาการอ่อนเพลียตอนกลางวันหรือไม่')

    routine_one = RadioField(u'Feeding (รับประทานอาหารเมื่อเตรียมสำรับไว้ล่วงหน้า)', choices=[
        (0, u'ไม่สามารถตักอาหารเข้าปากได้ ต้องมีคนป้อนให้'),
        (1, u'ตักอาหารเองได้แต่ต้องมีคนช่วย เช้น ช่วยใช้ช้อนตักเตรียมไว้ให้หรือตัดเป็นเล็กๆไว้ล่วงหน้า'),
        (2, u'ตักอาหารและช่วยตัวเองได้เป็นปกติ')
        ])

    routine_two = RadioField(u'Grooming (ล้างหน้า หวีผม แปรงฟัน โกนหนวดในระยะเวลา 24-48 ชม.ที่ผ่านมา)',
            choices=[
                (0, u'ต้องการความช่วยเหลือ'),
                (1, u'ทำเองได้ หรือทำเองได้ถ้าเตรียมอุปกรณ์ไว้ให้')
                ])

    routine_three = RadioField(u'Transfer (ลุกจากที่นอนหรือเตียงไปที่เก้าอี้)',
            choices=[
                (0, u'ไม่สามารถนั่งได้ นั่งแล้วจะล่มเสมอ หรือต้องใช้สองคนช่วยกันยกขึ้น'),
                (1, u'ต้องการความช่วยเหลืออย่างมากจึงจะนั่งได้เช่นต้องใช้คนที่แข็งแรงหรือมีทักษะ 1 คน หรือใช้คนทั่วไป 2 คนพยุง'),
                (2, u'ต้องการความช่วยเหลือบ้างเช่น บอกให้ทำตาม หรือช่วยพยุงเล็กน้อยหรือต้องมีคนดูแลเพื่อความปลอดภัย')
                ])

    routine_four = RadioField(u'Toilet use (ใช้ห้องน้ำ)',
            choices=[
                (0, u'ช่วยตัวเองไม่ได้'),
                (1, u'ทำเองได้บ้าง (อย่างน้อยทำความสะอาดตัวเองได้หลังเสร็จธุระ) แต่ต้องการความช่วยเหลือในบางสื่ง'),
                (2, u'ช่วยตัวเองได้ดี (ขึ้นนั่งและลงจากโถส้วมเองได้ ทำความสะอาดได้เรียบร้อยหลังเสร็จธุระ ถอดใส่เสื้อผ้าได้เรียบร้อย)')
                ])

    routine_five = RadioField(u'Mobility (การเคลื่อนที่ภายในห้องหรือบ้าน)',
            choices=[
                (0, u'เคลื่อนที่ไปไหนไม่ได้'),
                (1, u'ต้องใช้รถเข็นช่วยตัวเองให้เคลื่อนที่ได้เอง (ไม่ต้องมีคนเข็นให้) และเข้าออกมุมห้องหรือประตูได้'),
                (2, u'เดินหรือเคลื่อนที่โดยมีตนช่วย เช้น พยุง หรือบอกให้ทำตาม หรือต้องให้ความสนใจ ดูแลเพื่อความปลอดภัย'),
                (3, u'เดินหรือเคลื่อนที่ได้เอง')
                ])

    routine_six = RadioField(u'Dressing (การสวมใส่เสื้อผ้า)',
            choices=[
                (0, u'ต้องมีคนสวมใส่ให้ ช่วยต้วเองแทบไม่ได้หรือได้น้อย'),
                (1, u'ช่วยตัวเองได้ประมาณร้อยละ 50 ที่เหลือต้องมีคนช่วย'),
                (2, u'ช่วยตัวเองได้ดี (รวมทั้งการติดกระดุม รูดซิบ หรือใช้เสื้อผ้าที่ดัดแปลงให้เหมาะสมก็ได้)')
                ])

    routine_seven = RadioField(u'Stairs (การขึ้นลงบันได 1 ขั้น)',
            choices=[
                (0, u'ไม่สามารถทำได้'),
                (1, u'ต้องการคนช่วย'),
                (2, u'ขึ้นลงเองได้ (ถ้าต้องใช้เครื่องช่วยเดิน เช่น walker จะต้องเอาขึ้นลงได้ด้วย)')
                ])

    routine_eight = RadioField(u'Bathing (การอาบน้ำ)',
            choices=[
                (0, u'ต้องมีคนด้วยหรือทำให้'),
                (1, u'อาบเองได้')
                ])

    routine_nine = RadioField(u'Bowels (การกลั้นการถ่ายอุจจาระในระยะ 1 สัปดาห์ที่ผ่านมา)',
            choices=[
                (0, u'กลั้นไม่ได้ หรือต้องการการสวนอุจจาระอยู่เสมอ'),
                (1, u'กลั้นไม่ได้บางครั้ง (เป็นน้อยกว่า 1 ครั้งต่อสัปดาห์)'),
                (2, u'กลั้นได้ปกติ')
                ])

    routine_ten = RadioField(u'Bladder (การกลั้นปัสสาวะในระยะ 1 สัปดาห์ที่ผ่านมา)',
            choices=[
                (0, u'กลั้นไม่ได้ หรือต้องการการสวนอุจจาระอยู่เสมอ'),
                (1, u'กลั้นไม่ได้บางครั้ง (เป็นน้อยกว่า 1 ครั้งต่อสัปดาห์)'),
                (2, u'กลั้นได้ปกติ')
                ])

    long_term_care_one_one = RadioField(u'การอยู่อาศัย หรือผู้ดูแลเมื่อเจ็บป่วย',
            choices=[
                (0, u'ไม่ได้อยู่คนเดียว หรือ มีคนดูแลเมื่อเจ็บป่วย'),
                (1, u'อยู่คนเดียว หรือไม่มีคนดูแลเมื่อเจ็บป่วย')
                ])

    long_term_care_one_two = RadioField(u'ลักษณะที่อยู่อาศัย',
            choices=[
                (0, u'มั่นคงแข็งแรง หรือไม่มั่นคงแต่ไม่มีผลต่อความปลอดภัยในชีวิตและสุขภาพ'),
                (1, u'ไม่มีที่อยู่อาศัยหรือมีที่อยู่อาศัยแต่ไม่ปลอดภัยต่อสุขภาพ')
                ])

    long_term_care_one_three = RadioField(u'ความเพียงพอของรายได้ในการดำเนินชีวิตประจำวัน',
            choices=[
                (0, u'เพียงพอ'),
                (1, u'ไม่เพียงพอ')
                ])

    long_term_care_two_one = RadioField(u'ความสามารถในการมองเห็น',
            choices=[
                (0, u'ชัดเจนโดยไม่ต้องใส่แว่น'),
                (0, u'ชัดเจนแต่ต้องใส่แว่น'),
                (0, u'ไม่ชัดเจนแต่ไม่มีปัญหาในการทำชีวิตประจำวัน'),
                (1, u'ไม่ชัดเจนและมีปัญหาในการทำกิจกรรมประจำวัน'),
                (1, u'ไม่เห็นเลย'),
                ])

    long_term_care_two_two = RadioField(u'ชัดเจนโดยไม่ต้องใข้เครื่องช่วย',
            choices=[
                (0, u'ชัดเจนโดยไม่ต้องใช้เครื่องช่วยฟัง'),
                (0, u'ชัดเจนแต่ไม่ต้องใช้เครื่องช่วยฟัง'),
                (0, u'ไม่ชัดเจนแต่ไม่มีปัญหาในการทำชีวิตประจำวัน'),
                (1, u'ไม่ชัดเจนและมีปัญหาในการทำกิจกรรมประจำวัน'),
                (1, u'ไม่ได้ยินเลย'),
                ])

    long_term_care_three_one = RadioField(u'มีอาการหลงลืม/ลืมเหตุการณ์ที่เพิ่งเกิดขึ้น เช่นกินข้าวแล้วบอกยังไม่ได้กิน',
            choices=[
                (0, u'ไม่มี'),
                (1, u'มี')
                ])

    long_term_care_three_two_one = BooleanField(u'หดหู่เศร้า หรือท้อแท้สิ้นหวัง')
    long_term_care_three_two_two = BooleanField(u'เบื่อทำอะไรก็ไม่เพลิน')

    submit = SubmitField('Submit')
