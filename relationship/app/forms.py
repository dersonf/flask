from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from app.models import User


class TipoForm(FlaskForm):
    tipo = StringField('Tipo de vegetal', validators=[DataRequired()])
    submit = SubmitField('Adicionar')


class AlimentoForm(FlaskForm):
    alimento = StringField('Alimento', validators=[DataRequired()])
    # Faz um SelectField dinamico
    tipos = SelectField(u'Tipos', coerce=int)
    submit = SubmitField('Salvar')


class UserLoginForm(FlaskForm):
    message = 'Campo obrigatório'
    username = StringField('Usuário',
        validators=[DataRequired(message=message)])
    password = PasswordField('Senha',
        validators=[DataRequired(message=message)])
    submit = SubmitField('Login')


class RegistroUsuarioForm(FlaskForm):
    message_username = 'Pelo menos 3 letras'
    message_password = 'As senhas estão diferentes'
    username = StringField('Usuário',
        validators=[DataRequired(), Length(min=3, message=message_username)])
    fullname = StringField('Nome completo', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password_again = PasswordField('Confirmar senha',
        validators=[DataRequired(),
        EqualTo('password', message=message_password)])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        '''Valida se username é único'''
        user = User.query.filter_by(username=username.data).first()
        # Se o user não estiver vazio vai lançar esse erro
        if user is not None:
            raise ValidationError('Utilize outro username, usuário já existe')


class PerfilForm(FlaskForm):
    fullname = StringField('Nome completo', validators=[DataRequired()])
    submit = SubmitField('Atualizar')
