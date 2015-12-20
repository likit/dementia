import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from . import login_manager
from flask.ext.login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def generate_confirmation_token(pid, expiration=3600):
    s = Serializer(current_app.config['SECRET_KEY'], expiration)
    return s.dumps({'confirm': pid})

def confirm(user, token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if data.get('confirm') != user['pid']:
        return False
    # TODO: read data from mongo db and update verify field
    user['verified'] = True
    return True


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(13))
    title = db.Column(db.String(30))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    province = db.Column(db.String(255))
    role = db.Column(db.String(20))
    org = db.Column(db.String(255))
    position = db.Column(db.String(255))
    phone = db.Column(db.String(25))
    cell = db.Column(db.String(25))
    verified = db.Column(db.Boolean)
    last_login = db.Column(db.DateTime)
    org_address = db.Column(db.String(255))
    moo = db.Column(db.String(255))
    province = db.Column(db.String(255))
    amphur = db.Column(db.String(255))
    district = db.Column(db.String(255))
    objective = db.Column(db.Text)
    updated_on = db.Column(db.DateTime)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

