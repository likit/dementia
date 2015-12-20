# -*- coding: utf_8 -*-
import csv
import sys
import os

from sqlalchemy import *
from app import create_app, db

webapp = create_app('default')
db.app = webapp


class Region(db.Model):
    __tablename__ = 'ref_regions'
    id = db.Column(Integer, primary_key=True)
    desc = db.Column(db.String(255))

    def __repr__(self):
        return '<Region %d %s>' % (self.id, self.desc)


class QuestionType(db.Model):
    __tablename__ = 'eh_question_types'
    id = Column(Integer, primary_key=True)
    th_name = Column(String(80))
    en_name = Column(String(80))
    remark = Column(String(40))
    group = Column(Integer)
    questions = db.relationship('Question', backref='question_type',
            lazy='dynamic')


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

    def __repr__(self):
        return '<Answer %d>' % self.id


class QuestionHealth(db.Model):
    __tablename__=  'eh_question_healths'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))
    parent_qh_id_ = db.Column(db.Integer)
    answers = db.relationship('AnswerHealth',
            backref='question')


class AnswerHealth(db.Model):
    __tablename__ = 'eh_answer_healths' # table name is maintaiend for reference.
    id = db.Column(Integer, primary_key=True)
    seq_ = db.Column(Integer)
    desc = db.Column(String(255))
    question_id = db.Column(db.Integer,
            db.ForeignKey('eh_question_healths.id'))
    other_ = db.Column(db.Boolean)
    disease_ = db.Column(db.Boolean)

    def __repr__(self):
        return '<Answer %d>' % self.id

def insert_question_type(infile):
    reader = csv.reader(open(infile))
    for row in reader:
        qt = QuestionType(th_name=unicode(row[1], 'utf8'),
                            en_name=row[2],
                            remark=unicode(row[3], 'utf8'),
                            group=row[4])
        db.session.add(qt)
        db.session.commit()


def insert_question(infile):
    reader = csv.reader(open(infile))
    n = 0
    for row in reader:
        q = Question(qname=unicode(row[1], 'utf8'),
                            question_type_id=row[2],
                            parent_qid=row[3],
                            order=row[4],
                            special=unicode(row[5], 'utf8'))
        db.session.add(q)
        db.session.commit()
        n += 1
        if n == 5: break

def insert_answer(infile):
    reader = csv.reader(open(infile))
    n = 0
    for row in reader:
        ans = Answer(
                score=row[1],
                desc=unicode(row[2], 'utf8'),
                question_id=row[3],
                order=row[4],
                text_=unicode(row[5], 'utf8'),
                other_=unicode(row[6], 'utf8'),
                )
        db.session.add(ans)
        db.session.commit()
        n += 1
        if n == 5: break


def to_bool(str_value):
    keys = {'N': False, 'Y': True}
    return keys[str_value]


def insert_question_health(infile):
    reader = csv.reader(open(infile))
    n = 0
    for row in reader:
        ans = QuestionHealth(
                id=row[0],
                desc=unicode(row[1], 'utf8'),
                parent_qh_id_=row[2]
                )
        db.session.add(ans)
        db.session.commit()


def insert_answer_health(infile):
    reader = csv.reader(open(infile))
    n = 0
    for row in reader:
        ans = AnswerHealth(
                id=row[0],
                seq_=row[1],
                desc=unicode(row[2], 'utf8'),
                question_id=row[3],
                other_=to_bool(unicode(row[4], 'utf8')),
                disease_=to_bool(unicode(row[5], 'utf8')),
                )
        db.session.add(ans)
        n += 1
        if n == 5: break
    db.session.commit()

def insert_data(infile, model, values):
    reader = csv.reader(open(infile))
    n = 0
    for row in reader:
        kwargs = {}
        for k,v in values.iteritems():
            kwargs[k] = v(row)

        r = model(**kwargs)
        db.session.add(r)
        print("{0} {1}".format(r.id, r.desc.encode('utf8')))
        n += 1
        if n == 5: break
    db.session.commit()


def main():
    try:
        db.create_all()
    except Exception as e:
        raise e
    else:
        print('SQLite is set.')
        datadir = '../data-latest'
        # insert_question_type(os.path.join(datadir,
        #                                 'eh_question_type.csv'))

        # insert_question(os.path.join(datadir, 'eh_question.csv'))
        # insert_answer(os.path.join(datadir, 'eh_answer.csv'))
        # insert_answer_health(os.path.join(datadir, 'eh_answer_health.csv'))
        # insert_question_health(os.path.join(datadir, 'eh_question_health.csv'))

        region_values = {
                'id': lambda x: x[0],
                'desc': lambda x: unicode(x[1], 'utf8'),
                }
        insert_data(os.path.join(datadir, 'ref_region.csv'),
                Region, region_values)

        # for row in Question.query.all():
        #     print("{0} {1}".format(row.id, row.qname.encode('utf8')))

        # for row in Answer.query.get_by(question_id=1):
        #     print("{0} {1} {2}".format(row.id, row.desc.encode('utf8'),
        #             row.question.qname.encode('utf8')))


if __name__=='__main__':
    main()
