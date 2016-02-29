from app import db
import datetime

class Elder(db.Model):
    __tablename__ = 'elders'
    id = db.Column(db.Integer, primary_key=True)
    updated_date = db.Column(db.DateTime)
    title = db.Column(db.String(128))
    firstname = db.Column(db.String(128))
    lastname = db.Column(db.String(128))
    pid = db.Column(db.String(13))
    address = db.Column(db.String(128))
    moo = db.Column(db.String(30))
    amphur = db.Column(db.String(255))
    district = db.Column(db.String(255))
    province = db.Column(db.String(255))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    gender = db.Column(db.String(30))
    marital = db.Column(db.String(30))
    marital_other = db.Column(db.String(30))
    edu = db.Column(db.Integer)
    edu_other = db.Column(db.String(255))
    edu_years = db.Column(db.Integer)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer, db.ForeignKey('question_groups.id'))
    question = db.Column(db.String(255))


class AnswerForm(db.Model):
    __tablename__ = 'answer_forms'
    id = db.Column(db.Integer, primary_key=True)
    collected_date = db.Column(db.DateTime)
    elder_id = db.Column(db.Integer, db.ForeignKey('elders.id'))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    updated_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    living = db.Column(db.String(128))
    living_caregiver = db.Column(db.String(128))
    living_other = db.Column(db.String(128))
    income = db.Column(db.String(128))
    elder_club = db.Column(db.String(128))
    health_status = db.Column(db.String(128))

    smoking = db.Column(db.String(128))
    smoke_freq = db.Column(db.String(128))
    smoke_per_week = db.Column(db.Integer)
    smoker_per_day = db.Column(db.Integer)
    smoke_years = db.Column(db.Integer)
    quit_smoke_years = db.Column(db.Integer)

    alcohol = db.Column(db.String(128))
    drink_per_day = db.Column(db.Integer)
    drink_years = db.Column(db.Integer)
    quit_drink_years = db.Column(db.Integer)

    congenital_disease = db.Column(db.String(128))
    congenital_dis_other = db.Column(db.String(128))
    congenital_dis_years = db.Column(db.Integer)

    fpg_level = db.Column(db.Float)
    fcg_level = db.Column(db.Float)
    systolic = db.Column(db.Integer)
    diastolic = db.Column(db.Integer)
    smoke_screening = db.Column(db.Boolean)
    bp = db.Column(db.Boolean)
    fpg = db.Column(db.Boolean)
    abnormal_lipid = db.Column(db.Boolean)
    waist = db.Column(db.Boolean)
    infarction = db.Column(db.Boolean)
    family_infarction = db.Column(db.Boolean)

    dental_brushing = db.Column(db.String(128))

    dental_brushing_gt_twice = db.Column(db.Integer)
    dental_brushing_other = db.Column(db.String(128))
    fluoride_toothpaste = db.Column(db.Boolean)
    dental_floss = db.Column(db.Boolean)
    dental_floss_equip = db.Column(db.String(128))
    smoke_ten_cig = db.Column(db.Boolean)
    chew_gum = db.Column(db.Boolean)

    dental_part_two_one = db.Column(db.Integer)
    dental_part_two_two = db.Column(db.Integer)
    dental_part_two_three = db.Column(db.Integer)
    dental_part_two_four = db.Column(db.Integer)
    dental_part_two_five = db.Column(db.Integer)
    dental_part_two_six = db.Column(db.Integer)
    dental_part_two_seven = db.Column(db.Integer)
    dental_part_two_one_follow_up = db.Column(db.Boolean)
    dental_part_two_two_follow_up = db.Column(db.Boolean)
    dental_part_two_three_follow_up = db.Column(db.Boolean)
    dental_part_two_four_follow_up = db.Column(db.Boolean)
    dental_part_two_five_follow_up = db.Column(db.Boolean)
    dental_part_two_six_follow_up = db.Column(db.Boolean)
    dental_part_two_seven_follow_up = db.Column(db.Boolean)
    dental_transfer_tissue = db.Column(db.Boolean)
    dental_transfer_gum = db.Column(db.Boolean)
    dental_transfer_cavity = db.Column(db.Boolean)
    dental_transfer_swallow = db.Column(db.Boolean)
    dental_transfer_denture = db.Column(db.Boolean)

    eye_exam_one = db.Column(db.Boolean)
    eye_exam_two = db.Column(db.Boolean)
    eye_exam_three = db.Column(db.Boolean)
    eye_exam_four = db.Column(db.Boolean)
    eye_exam_five = db.Column(db.Boolean)
    eye_exam_three_side = db.Column(db.String(20))
    eye_exam_four_side = db.Column(db.String(20))
    eye_exam_five_side = db.Column(db.String(20))
    snellen_left = db.Column(db.Integer)
    snellen_right = db.Column(db.Integer)

    amt_one = db.Column(db.Boolean)
    amt_two = db.Column(db.Boolean)
    amt_three = db.Column(db.Boolean)
    amt_four = db.Column(db.Boolean)
    amt_five = db.Column(db.Boolean)
    amt_six = db.Column(db.Boolean)
    amt_seven = db.Column(db.Boolean)
    amt_eight = db.Column(db.Boolean)
    amt_nine = db.Column(db.Boolean)
    amt_ten = db.Column(db.Boolean)

    mmse_one_one = db.Column(db.Integer)
    mmse_one_two = db.Column(db.Integer)
    mmse_one_three = db.Column(db.Integer)
    mmse_one_four = db.Column(db.Integer)

    mmse_two_one_one = db.Column(db.Integer)
    mmse_two_one_two = db.Column(db.Integer)
    mmse_two_one_three = db.Column(db.Integer)
    mmse_two_one_four = db.Column(db.Integer)
    mmse_two_one_five = db.Column(db.Integer)

    mmse_two_two_one = db.Column(db.Integer)
    mmse_two_two_two = db.Column(db.Integer)
    mmse_two_two_three = db.Column(db.Integer)
    mmse_two_two_four = db.Column(db.Integer)
    mmse_two_two_five = db.Column(db.Integer)

    mmse_three_flower = db.Column(db.Boolean)
    mmse_three_river = db.Column(db.Boolean)
    mmse_three_train = db.Column(db.Boolean)
    mmse_three_tree = db.Column(db.Boolean)
    mmse_three_sea = db.Column(db.Boolean)
    mmse_three_car = db.Column(db.Boolean)

    mmse_four_one = db.Column(db.Integer)
    mmse_four_two = db.Column(db.Integer)

    mmse_five_flower = db.Column(db.Boolean)
    mmse_five_river = db.Column(db.Boolean)
    mmse_five_train = db.Column(db.Boolean)
    mmse_five_tree = db.Column(db.Boolean)
    mmse_five_sea = db.Column(db.Boolean)
    mmse_five_car = db.Column(db.Boolean)

    mmse_six_one = db.Column(db.Integer)
    mmse_six_two = db.Column(db.Integer)
    mmse_seven_one = db.Column(db.Integer)

    mmse_eight_one = db.Column(db.Boolean)
    mmse_eight_two = db.Column(db.Boolean)
    mmse_eight_three = db.Column(db.Boolean)
    mmse_nine_one = db.Column(db.Boolean)
    mmse_ten_one = db.Column(db.Boolean)
    mmse_eleven_one = db.Column(db.Boolean)

    q2_one = db.Column(db.Boolean)
    q2_two = db.Column(db.Boolean)

    q9_one = db.Column(db.Integer)
    q9_two = db.Column(db.Integer)
    q9_three = db.Column(db.Integer)
    q9_four = db.Column(db.Integer)
    q9_five = db.Column(db.Integer)
    q9_six = db.Column(db.Integer)
    q9_seven = db.Column(db.Integer)
    q9_eight = db.Column(db.Integer)
    q9_nine = db.Column(db.Integer)

    knee_pain = db.Column(db.Integer)
    knee_pain_clinic_one = db.Column(db.Boolean)
    knee_pain_clinic_two = db.Column(db.Boolean)
    knee_pain_clinic_three = db.Column(db.Boolean)
    knee_pain_clinic_four = db.Column(db.Boolean)
    knee_pain_clinic_five = db.Column(db.Boolean)

    tugt = db.Column(db.Integer)
    urine_holding = db.Column(db.Integer)
    bmi = db.Column(db.Integer)
    malnutrition_one = db.Column(db.Integer)
    malnutrition_two = db.Column(db.Integer)
    malnutrition_three = db.Column(db.Integer)
    malnutrition_four = db.Column(db.Integer)
    malnutrition_five = db.Column(db.Integer)
    malnutrition_six = db.Column(db.Integer)

    sleeping_one = db.Column(db.Integer)
    insomnia = db.Column(db.Boolean)
    oversleep = db.Column(db.Boolean)
    snore = db.Column(db.Boolean)
    dreamwalk = db.Column(db.Boolean)
    sleeping_other = db.Column(db.String(128))
    sleeping_period_year = db.Column(db.Integer)
    sleeping_period_month = db.Column(db.Integer)
    sleeping_avg_hours = db.Column(db.Integer)
    fatique = db.Column(db.Boolean)

    routine_one = db.Column(db.Integer)
    routine_two = db.Column(db.Integer)
    routine_three = db.Column(db.Integer)
    routine_four = db.Column(db.Integer)
    routine_five = db.Column(db.Integer)
    routine_six = db.Column(db.Integer)
    routine_seven = db.Column(db.Integer)
    routine_eight = db.Column(db.Integer)
    routine_nine = db.Column(db.Integer)
    routine_ten = db.Column(db.Integer)

    long_term_care_one_one = db.Column(db.Integer)
    long_term_care_one_two = db.Column(db.Integer)
    long_term_care_one_three = db.Column(db.Integer)
    long_term_care_two_one = db.Column(db.Integer)
    long_term_care_two_two = db.Column(db.Integer)
    long_term_care_three_one = db.Column(db.Integer)
    long_term_care_three_two_one = db.Column(db.Boolean)
    long_term_care_three_two_two = db.Column(db.Boolean)

    long_term_care_four_one = db.Column(db.Boolean)
    long_term_care_four_two = db.Column(db.Boolean)
    long_term_care_four_three = db.Column(db.Boolean)
    long_term_care_four_four = db.Column(db.Boolean)
    long_term_care_four_five = db.Column(db.Boolean)

    long_term_care_five_one = db.Column(db.Integer)
    long_term_care_five_two = db.Column(db.Integer)
    long_term_care_five_three = db.Column(db.Integer)
    long_term_care_five_four = db.Column(db.Integer)
    long_term_care_five_five = db.Column(db.Integer)
    long_term_care_five_six = db.Column(db.Integer)
    long_term_care_five_seven = db.Column(db.Integer)
    long_term_care_five_eight = db.Column(db.Integer)
    long_term_care_five_nine = db.Column(db.Integer)
    long_term_care_five_ten = db.Column(db.Integer)
    long_term_care_five_eleven = db.Column(db.Integer)
    long_term_care_five_twelve = db.Column(db.Integer)
    long_term_care_five_thirteen = db.Column(db.Integer)
    long_term_care_five_fourteen = db.Column(db.Integer)
    long_term_care_five_fifteen = db.Column(db.Integer)
    long_term_care_five_sixteen = db.Column(db.Integer)

    locale = db.Column(db.String(255))


class QuestionGroup(db.Model):
    __tablename__ = 'question_groups'
    id = db.Column(db.Integer, primary_key=True)


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    # question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    form_id = db.Column(db.Integer, db.ForeignKey('answer_forms.id'))
