from flask import render_template, flash, redirect, url_for
# carregando o Flask-Login
from flask_login import current_user, login_user
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        'index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Verifica se o usuário já está autenticado
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Carrega o form para ser preenchido
    form = LoginForm()
    '''Se for GET recebe False, se for POST recebe True e valida o form
    se der algum erro retorna False'''
    if form.validate_on_submit():
        # Busca o usuário na base de dados
        user = User.query.filter_by(username=form.username.data).first()
        # Valida se o usuário existe ou se a senha foi preenchida
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Exibe mensagem para o usuário, o template precisa ter o get desse componente
        # flash(f"Login requestd for user {form.username.data}, remember_me={form.remember_me.data}")
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)