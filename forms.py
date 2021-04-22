from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms.validators import Length


class TaskForm(Form):
    name = StringField('Nombre', validators=[Length(min=4, max=25)])