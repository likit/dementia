from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from . import login_manager
from flask.ext.login import UserMixin


class LoginUser():
    def __init__(self, username):
            self.username = username

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

class User():
    def __init__(self, username, **kwargs):
        if kwargs['role'] != 'admin':
            self.username = username
            self.province = kwargs['province']
            self.name = kwargs['name']
            self.lastname = kwargs['lastname']
            self.title = kwargs['title']
            self.role = kwargs['role']
            self.position = kwargs['position']
            self.org = kwargs['org']
            self.verified = kwargs['verified']
        elif kwargs['role'] == 'admin':
            self.username = username
            self.role = 'admin'
        else:
            pass

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

@login_manager.user_loader
def load_user(username):
    u = db.users.find_one({'username': username})
    if not u:
        return None
    else:
        if u['role'] != 'admin':
            return User(u['username'], title=u['title'], name=u['name'],
                    lastname=u['lastname'], province=u['province'],
                    role=u['role'], org=u['org'], position=u['position'],
                    verified=u['verified'])
        elif u['role'] == 'admin':
            return User(u['username'], email=u['email'], role=u['role'])
        else:
            pass


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
