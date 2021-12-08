from flask_wtf import FlaskForm
from wtforms import StringField


class AutoCompleteForm(FlaskForm):
    nome = StringField('Nome', id='autocomplete')
