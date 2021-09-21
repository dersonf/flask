from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired


class TipoForm(FlaskForm):
    tipo = StringField('Tipo de vegetal', validators=[DataRequired()])
    submit = SubmitField('Salvar')


class AlimentoForm(FlaskForm):
    alimento = StringField('Alimento', validators=[DataRequired()])
    # Faz um SelectField dinamico
    tipos = SelectField(u'Tipos', coerce=int)
    submit = SubmitField('Salvar')


class UserLoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')
