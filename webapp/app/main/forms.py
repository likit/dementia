from flask.ext.wtf import Form
from wtforms.validators import Required, NumberRange, Optional
from wtforms import StringField, SubmitField, IntegerField

class Form1(Form):
    name = StringField('Name', validators=[Required()])
    community = StringField('Community', validators=[Optional()])
    district = StringField('District', validators=[Required()])
    title = StringField('Title', validators=[Required()])
    age = IntegerField('Age', validators=[Required(), NumberRange(1,130)])
    weight = IntegerField('Weight', validators=[Required()])
    height = IntegerField('Height', validators=[Required(),
        NumberRange(50,220)])
    submit = SubmitField('Submit')
