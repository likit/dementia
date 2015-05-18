#!/usr/bin/env python

import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash
from datetime import datetime

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def initdb():
    """Init the database."""
    db.drop_collection('users')
    db.drop_collection('form1')
    password = generate_password_hash('testpass')
    admin_doc = {
                'username': 'admin',
                'email': 'admin@example.com',
                'password': password,
                'name': 'Likit',
                'lastname': 'Preeyanon',
                'organization': 'MUMT',
                'role': 'admin',
                'zone': -1,
                'verified': True,
                'create_date_time': datetime.today(),
            }

    db.users.insert(admin_doc, safe=True)

if __name__ == '__main__':
    manager.run()
