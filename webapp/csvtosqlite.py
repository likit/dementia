# -*- coding: utf_8 -*-
import csv
import sys
import os

from sqlalchemy import *
from app import create_app, db

webapp = create_app('default')
db.app = webapp

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

        insert_question(os.path.join(datadir, 'eh_question.csv'))
        insert_answer(os.path.join(datadir, 'eh_answer.csv'))


if __name__=='__main__':
    main()
