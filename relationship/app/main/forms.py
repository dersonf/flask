from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class TipoForm(FlaskForm):
    tipo = StringField('Tipo de vegetal', validators=[DataRequired()])
    submit = SubmitField('Adicionar')


class AlimentoForm(FlaskForm):
    alimento = StringField('Alimento', validators=[DataRequired()])
    # Faz um SelectField dinamico
    tipos = SelectField(u'Tipos', coerce=int)
    submit = SubmitField('Salvar')
