from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Name(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    submit = SubmitField('OK')

    def check_nome(form, nome):
        if not nome.data:
            raise ValidationError('Teste')

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
