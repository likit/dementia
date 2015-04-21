from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask.ext.login import LoginManager
from config import config
import pymongo

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
admin = Admin()
conn = pymongo.Connection()
db = conn['data-dev']
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from main.views import UserView
    admin.add_view(UserView(db.users, 'User'))

    from main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
