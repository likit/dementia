from werkzeug.security import generate_password_hash, check_password_hash
from . import db

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
