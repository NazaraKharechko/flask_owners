from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class RegisterOwner(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'name must be 2-20 characters')])
    age = IntegerField('Age', [DataRequired(), NumberRange(10, 120, 'age range must be 10-120')])
    city = StringField('City', [DataRequired(), length(3, 20, 'city must be 3-20 characters')])
    save = SubmitField('Save')


class RegisterPet(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'name must be 2-20 characters')])
    age = IntegerField('Age', [DataRequired(), NumberRange(1, 50, 'age range must be 1-50')])
    animal_type = StringField('Animal Type', [DataRequired(), length(2, 20, 'city must be 2-20 characters')])
    save = SubmitField('Save')
