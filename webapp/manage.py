#!/usr/bin/env python

import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash

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
def dbinit():
    """Init the database."""
    db.drop_collection('users')
    password = generate_password_hash('hardtoguess')
    user_doc = {
            'username': 'admin',
            'email': 'likit.pre@mahidol.edu',
            'password': password,
            'role': 'admin',
            'zone': 0,
            }
    db.users.insert(user_doc, safe=True)

if __name__ == '__main__':
    manager.run()
