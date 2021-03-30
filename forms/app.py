from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, InputRequired
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# Formulários
class NameForm(FlaskForm):
    nome = StringField(label='nome', validators=[DataRequired
        (message='Precisa ser preenchido')], default='anderson')
    submit = SubmitField('OK')

    def validate_nome(form, field):
        if len(field.data) < 3:
            raise ValidationError('Nome só com duas letras?')


class CheckboxBaseForm(FlaskForm):
    checkbox = BooleanField('Nome do cão')
    # checkbox1 = BooleanField('Nome do cão')
    submit = SubmitField('Aceito')

    def __init__(self, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.checkbox.label = label


@app.route('/')
def index():
    return render_template('index.html', nome=session.get('nome'))


@app.route('/login', methods=['GET', 'POST'])
def nome():
    form = NameForm()
    if form.validate_on_submit():
        # url_for vai usar a função ao inves do path
        # return redirect('/')
        session['nome'] = form.nome.data
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/checkbox', methods=['GET', 'POST'])
def checkbox():
    form = CheckboxBaseForm('pizza?')
    if form.validate_on_submit():
        if form.checkbox.data == True:
            session['checkbox'] = True
        else:
            session['checkbox'] = False
        return redirect(url_for('index'))
    return render_template('checkbox.html', title='Teste boolean', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
