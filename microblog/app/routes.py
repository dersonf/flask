from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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
    form = LoginForm()
    '''Se for GET recebe False, se for POST recebe True e valida o form
    se der algum erro retorna False'''
    if form.validate_on_submit():
        # Exibe mensagem para o usuário, o template precisa de ajustes
        flash(f"Login requestd for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)