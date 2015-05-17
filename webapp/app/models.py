from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from . import login_manager
from flask.ext.login import UserMixin

class User():
    def __init__(self, username, zone, role):
        self.username = username
        self.zone = zone
        self.role = role

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
    u = db.users.find_one({'username':username})
    if not u:
        return None
    return User(u['username'], u['zone'], u['role'])

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
