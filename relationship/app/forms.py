from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TipoForm(FlaskForm):
    tipo = StringField('Tipo de vegetal')
    submit = SubmitField('Salvar')


class AlimentoForm(FlaskForm):
    alimento = StringField('Alimento')
    submit = SubmitField('Salvar')
