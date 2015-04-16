from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from config import config
import pymongo

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
admin = Admin()
conn = pymongo.Connection()
db = conn['data-dev']

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    admin.init_app(app)

    from main.views import UserView
    admin.add_view(UserView(db.users, 'User'))

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
