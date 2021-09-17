from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from app.models import Tipo


class TipoForm(FlaskForm):
    tipo = StringField('Tipo de vegetal')
    submit = SubmitField('Salvar')


class AlimentoForm(FlaskForm):
    alimento = StringField('Alimento')
    # Faz um SelectField dinamico
    tipos = SelectField(u'Tipos', coerce=int)
    submit = SubmitField('Salvar')
