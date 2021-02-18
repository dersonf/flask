from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


class Name(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    submit = SubmitField('OK')


@app.route('/')
def index():
    return render_template('index.html', nome=session.get('nome'))


@app.route('/login', methods=['GET', 'POST'])
def nome():
    form = Name()
    if form.validate_on_submit():
        # url_for vai usar a função ao inves do path
        # return redirect('/')
        session['nome'] = form.nome.data
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    session.pop('nome', None)
    return redirect(url_for('index'))
