import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'center_of_data_mining'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SUBJECT_PREFIX = '[TEIS]'
    MAIL_SENDER = 'Likit Preeyanon <likit.pre@mahidol.edu>'
    ADMIN_EMAIL = 'likit.pre@mahidol.edu'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #         'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MONGO_DBNAME = 'data-dev'


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = \
    #         os.environ.get('TEST_DATABASE_URL') or \
    #         'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    MONGO_DBNAME = 'data-test'


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #         'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    MONGO_DBNAME = 'data'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
