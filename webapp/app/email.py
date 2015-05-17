from flask.ext.mail import Message
from flask import current_app
from flask import render_template
from . import mail

def send_email(to, subject, template, **kwargs):
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX'] + subject,
            sender=current_app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    mail.send(msg)
