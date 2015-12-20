# -*- coding: utf_8 -*-
import csv
import sys
import os

from sqlalchemy import *
from app import create_app, db

webapp = create_app('default')
db.app = webapp


class Elder(db.Model):
    __tablename__ = 'eh_elders'
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(30))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    birthday = db.Column(db.String(40))
    gender = db.Column(db.String(20))
    pid = db.Column(db.String(13))
    living = db.Column(db.Boolean)
    note = db.Column(db.Text)
    created_date = db.Column(db.String(40))
    created_by = db.Column(db.Integer, db.ForeignKey('eh_users.id'))
    updated_date = db.Column(db.String(40))
    updated_by = db.Column(db.Integer, db.ForeignKey('eh_users.id'))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    edu_id = db.Column(db.Integer, db.ForeignKey('ref_educations.id'))

    schema = {
            'id': lambda x: x[0],
            'prefix': lambda x: unicode(x[1], 'utf8'),
            'firstname': lambda x: unicode(x[2], 'utf8'),
            'lastname': lambda x: unicode(x[3], 'utf8'),
            'birthday': lambda x: unicode(x[4], 'utf8'),
            'gender': lambda x: unicode(x[5], 'utf8'),
            'pid': lambda x: unicode(x[6], 'utf8'),
            'living': lambda x: to_bool(unicode(x[7], 'utf8')),
            'note': lambda x: unicode(x[8], 'utf8'),
            'created_date': lambda x: unicode(x[9], 'utf8'),
            'created_by': lambda x: x[10],
            'updated_date': lambda x: unicode(x[11], 'utf8'),
            'updated_by': lambda x: x[12],
            'height': lambda x: x[13],
            'weight': lambda x: x[14],
            'edu_id': lambda x: unicode(x[15], 'utf8').isdigit() or None,
            }


class ElderAddr(db.Model):
    __tablename__ = 'eh_elder_addresses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(40))
    moo = db.Column(db.String(10))
    tel = db.Column(db.String(40))
    pad_id = db.Column(db.Integer, db.ForeignKey('pads.id'))
    elder_id = db.Column(db.Integer, db.ForeignKey('eh_elders.id'))
    current = db.Column(db.Boolean)
    updated_year = db.Column(db.String(10))
    village = db.Column(db.String(255))

    schema = {
            'id': lambda x: x[0],
            'address': lambda x: unicode(x[1], 'utf8'),
            'moo': lambda x: unicode(x[2], 'utf8'),
            'tel': lambda x: unicode(x[3], 'utf8'),
            'pad_id': lambda x: unicode(x[4], 'utf8').isdigit() or None,
            'elder_id': lambda x: unicode(x[5], 'utf8').isdigit() or None,
            'current': lambda x: to_bool(x[7]),
            'updated_year': lambda x: unicode(x[8], 'utf8'),
            'village': lambda x: unicode(x[9], 'utf8'),
            }



class User(db.Model):
    __tablename__ = 'eh_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(13))
    password = db.Column(db.String(40))
    prefix = db.Column(db.String(20))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    tel = db.Column(db.String(40))
    mobile = db.Column(db.String(40))
    email = db.Column(db.String(255))
    admin = db.Column(db.Boolean)
    location_id = db.Column(db.Integer, db.ForeignKey('eh_user_locations.id'))
    created_date = db.Column(db.String(255))
    created_by = db.Column(db.Integer, db.ForeignKey('eh_users.id'))
    updated_date = db.Column(db.String(255))
    updated_by = db.Column(db.Integer, db.ForeignKey('eh_users.id'))

    schema = {
            'id': lambda x: x[0],
            'username': lambda x: unicode(x[1], 'utf8'),
            'password': lambda x: None,
            'prefix': lambda x: unicode(x[3], 'utf8'),
            'firstname': lambda x: unicode(x[4], 'utf8'),
            'lastname': lambda x: unicode(x[5], 'utf8'),
            'tel': lambda x: unicode(x[6], 'utf8'),
            'mobile': lambda x: unicode(x[7], 'utf8'),
            'email': lambda x: unicode(x[8], 'utf8'),
            'admin': lambda x: to_bool(unicode(x[9], 'utf8')),
            'location_id': lambda x: unicode(x[10], 'utf8').isdigit() or None,
            'created_date': lambda x: unicode(x[11], 'utf8'),
            'created_by': lambda x: x[12],
            'updated_date': lambda x: unicode(x[13], 'utf8'),
            'updated_by': lambda x: x[14],
            }


class UserLocation(db.Model):
    __tablename__ = 'eh_user_locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    moo = db.Column(db.String(10))
    pad_id = db.Column(db.Integer, db.ForeignKey('pads.id'))
    users = db.relationship('User', backref='location', lazy='dynamic')

    schema = {
            'id': lambda x: x[0],
            'name': lambda x: unicode(x[1], 'utf8'),
            'address': lambda x: unicode(x[2], 'utf8'),
            'moo': lambda x: unicode(x[3], 'utf8'),
            'pad_id': lambda x: unicode(x[4], 'utf8').isdigit() or None,
            }


class Education(db.Model):
    __tablename__ = 'ref_educations'
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(255))
    level = db.Column(db.Integer)
    edu = db.relationship('Elder', backref='education', lazy='dynamic')
    schema = {
            'id': lambda x: x[0],
            'degree': lambda x: unicode(x[1], 'utf8'),
            'level': lambda x: x[2],
            }


class Region(db.Model):
    __tablename__ = 'ref_regions'
    id = db.Column(Integer, primary_key=True)
    desc = db.Column(db.String(255))
    provinces = db.relationship('Province', backref='region', lazy='dynamic')


    schema = {
            'id': lambda x: x[0],
            'desc': lambda x: unicode(x[1], 'utf8'),
            }

    def __repr__(self):
        return '<Region %d %s>' % (self.id, self.desc)


class Province(db.Model):
    __tablename__ = 'ref_provinces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    region_id = db.Column(db.Integer, db.ForeignKey('ref_regions.id'))
    pads = db.relationship('Pad', backref='province', lazy='dynamic')
    schema = {
            'id': lambda x: x[0],
            'name': lambda x: unicode(x[1], 'utf8'),
            'region_id': lambda x: unicode(x[2], 'utf8').isdigit() or None,
            }


class Amphur(db.Model):
    __tablename__ = 'ref_amphurs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pads = db.relationship('Pad', backref='amphur', lazy='dynamic')
    schema = {
            'id': lambda x: x[0],
            'name': lambda x: unicode(x[1], 'utf8'),
            }


class District(db.Model):
    __tablename__ = 'ref_districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pads = db.relationship('Pad', backref='district', lazy='dynamic')
    schema = {
            'id': lambda x: x[0],
            'name': lambda x: unicode(x[1], 'utf8'),
            }


class Pad(db.Model):
    __tablename__ = 'pads'
    id = db.Column(db.Integer, primary_key=True)
    province_id = db.Column(db.Integer, db.ForeignKey('ref_provinces.id'))
    amphur_id = db.Column(db.Integer, db.ForeignKey('ref_amphurs.id'))
    district_id = db.Column(db.Integer, db.ForeignKey('ref_districts.id'))
    schema = {
            'id': lambda x: x[0],
            'province_id': lambda x: unicode(x[1], 'utf8').isdigit() or None,
            'amphur_id': lambda x: unicode(x[2], 'utf8').isdigit() or None,
            'district_id': lambda x: unicode(x[3], 'utf8').isdigit() or None,
            }


class QuestionType(db.Model):
    __tablename__ = 'eh_question_types'
    id = Column(Integer, primary_key=True)
    th_name = Column(String(80))
    en_name = Column(String(80))
    remark = Column(String(40))
    group = Column(Integer)
    questions = db.relationship('Question', backref='question_type',
            lazy='dynamic')
    schema = {
            'id': lambda x: x[0],
            'th_name': lambda x: unicode(x[1], 'utf8'),
            'en_name': lambda x: unicode(x[2], 'utf8'),
            'remark': lambda x: unicode(x[3], 'utf8'),
            'group': lambda x: unicode(x[4], 'utf8'),
            }


class Question(db.Model):
    __tablename__ = 'eh_questions'
    id = Column(Integer, primary_key=True)
    qname = Column(String(255))
    parent_qid = Column(Integer)
    order = Column(Integer)
    special = Column(String(255))
    question_type_id = db.Column(Integer,
            db.ForeignKey('eh_question_types.id'))
    answers = db.relationship('Answer', backref='question')
    schema = {
            'id': lambda x: x[0],
            'qname': lambda x: unicode(x[1], 'utf8'),
            'question_type_id': lambda x: unicode(x[2],
                                    'utf8').isdigit() or None,
            'parent_qid': lambda x: unicode(x[3], 'utf8').isdigit() or None,
            'order': lambda x: x[4],
            'special': lambda x: unicode(x[5], 'utf8'),
            }


class Answer(db.Model):
    __tablename__ = 'eh_answers'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    desc = db.Column(db.String(255))
    order = db.Column(db.Integer)
    text_ = db.Column(db.String(40))
    other_ = db.Column(db.String(255))
    question_id = db.Column(db.Integer,
                        db.ForeignKey('eh_questions.id'))
    schema = {
            'id': lambda x: x[0],
            'score': lambda x: x[1],
            'desc': lambda x: unicode(x[2], 'utf8'),
            'question_id': lambda x: unicode(x[3], 'utf8').isdigit() or None,
            'order': lambda x: x[4],
            'text_': lambda x: unicode(x[5], 'utf8'),
            'other_': lambda x: unicode(x[6], 'utf8'),
            }

    def __repr__(self):
        return '<Answer %d>' % self.id


class QuestionHealth(db.Model):
    __tablename__=  'eh_question_healths'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))
    parent_qh_id_ = db.Column(db.Integer)
    answers = db.relationship('AnswerHealth',
            backref='question')
    schema = {
            'id': lambda x: x[0],
            'desc': lambda x: unicode(x[1], 'utf8'),
            'parent_qh_id_': lambda x: unicode(x[2], 'utf8').isdigit() or None,
            }


class AnswerHealth(db.Model):
    __tablename__ = 'eh_answer_healths' # table name is maintaiend for reference.
    id = db.Column(Integer, primary_key=True)
    seq_ = db.Column(Integer)
    desc = db.Column(String(255))
    question_id = db.Column(db.Integer,
            db.ForeignKey('eh_question_healths.id'))
    other_ = db.Column(db.Boolean)
    disease_ = db.Column(db.Boolean)
    schema = {
            'id': lambda x: x[0],
            'seq_': lambda x: x[1],
            'desc': lambda x: unicode(x[2], 'utf8'),
            'question_id': lambda x: unicode(x[3], 'utf8').isdigit() or None,
            'other_': lambda x: to_bool(unicode(x[4], 'utf8')),
            'disease_': lambda x: to_bool(unicode(x[5], 'utf8')),
            }

    def __repr__(self):
        return '<Answer %d>' % self.id

def to_bool(str_value):
    keys = {'N': False, 'Y': True}
    return keys.get(str_value, False)


def insert_data(infile, model):
    reader = csv.reader(open(infile))
    n = 0
    failed = 0
    for n, row in enumerate(reader):
        kwargs = {}
        for k,v in model.schema.iteritems():
            kwargs[k] = v(row)

        r = model(**kwargs)
        try:
            db.session.add(r)
            db.session.commit()
        except Exception as e:
            failed += 1
            raise e

        if n == 20: break

    print('Failed %d' % failed)


def main():
    try:
        db.drop_all()
        db.create_all()
    except Exception as e:
        raise e
    else:
        print('SQLite is set.')
        datadir = '../data-latest'
        print('Inserting question types')
        insert_data(os.path.join(datadir,
                                'eh_question_type.csv'), QuestionType)

        print('Inserting question')
        insert_data(os.path.join(datadir, 'eh_question.csv'),
                Question)
        print('Inserting answers')
        insert_data(os.path.join(datadir, 'eh_answer.csv'), Answer)
        print('Inserting answer health')
        insert_data(os.path.join(datadir, 'eh_answer_health.csv'),
                AnswerHealth)
        print('Inserting question health')
        insert_data(os.path.join(datadir, 'eh_question_health.csv'),
                QuestionHealth)

        print('Inserting regions')
        insert_data(os.path.join(datadir, 'ref_region.csv'), Region)

        print('Inserting provinces')
        insert_data(os.path.join(datadir, 'ref_province.csv'), Province)
        print('Inserting districts')
        insert_data(os.path.join(datadir, 'ref_district.csv'), District)
        print('Inserting amphurs')
        insert_data(os.path.join(datadir, 'ref_amphur.csv'), Amphur)
        print('Inserting pads')
        insert_data(os.path.join(datadir, 'ref_pad.csv'), Pad)
        print('Inserting educations')
        insert_data(os.path.join(datadir, 'ref_education.csv'), Education)

        print('Inserting elders')
        insert_data(os.path.join(datadir, 'eh_elder.csv'), Elder)
        print('Inserting elders address')
        insert_data(os.path.join(datadir, 'eh_elder_address.csv'), ElderAddr)
        print('Inserting user')
        insert_data(os.path.join(datadir, 'eh_user.csv'), User)
        print('Inserting user location')
        insert_data(os.path.join(datadir,
            'eh_user_location.csv'), UserLocation)

        # for row in Question.query.all():
        #     print("{0} {1}".format(row.id, row.qname.encode('utf8')))

        # for row in Answer.query.get_by(question_id=1):
        #     print("{0} {1} {2}".format(row.id, row.desc.encode('utf8'),
        #             row.question.qname.encode('utf8')))


if __name__=='__main__':
    main()
