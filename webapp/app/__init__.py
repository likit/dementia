import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../aging-test.db'
    app.config['SECRET_KEY'] = 'thegodfather'

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    ''' Views has to be imported after app instance has been created,
        otherwise relative import will not work.'''

    # from adminpage.views import UserView, MyAdminIndexView, Form1View, HomeView
    # admin = Admin(name='My Admin',
    #         index_view=MyAdminIndexView(endpoint='admin'))

    # admin.add_view(UserView(db.users, 'User'))
    # admin.add_view(Form1View(db.form1, 'Form1'))
    # admin.add_view(HomeView(name='App Home'))

    # admin.init_app(app)

    from main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
