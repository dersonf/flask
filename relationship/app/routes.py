from flask.helpers import url_for
from app import app, db, login
from flask import render_template, redirect, flash, request
from app.models import Alimento, Tipo, User
from app.forms import (
    TipoForm,
    AlimentoForm,
    UserLoginForm,
    RegistroUsuarioForm,
    PerfilForm,
    )
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    vegetais = Alimento.query.all()
    return render_template('index.html', vegetais=vegetais)


@app.route('/addtipo', methods=['GET', 'POST'])
@login_required
def addtipo():
    '''Adiciona o tipo de vegetal'''
    form = TipoForm()
    tipos = Tipo.query.all()
    if form.validate_on_submit():
        tipo = Tipo(tipo=form.tipo.data)
        db.session.add(tipo)
        flash(_commit())
        return redirect(url_for('addtipo'))
    return render_template('addtipo.html', form=form, tipos=tipos)


@app.route('/addalimento', methods=['GET', 'POST'])
@login_required
def addalimento():
    '''Adiciona o vegetal'''
    form = AlimentoForm()
    form.tipos.choices = [(t.id, t.tipo) for t in Tipo.query.order_by('tipo')]
    alimentos = Alimento.query.all()
    if form.validate_on_submit():
        tipo = Tipo.query.get(form.tipos.data)
        alimento = Alimento(alimento=form.alimento.data, tipo=tipo)
        db.session.add(alimento)
        flash(_commit())
        return redirect(url_for('addalimento'))
    return render_template('addalimento.html', form=form, alimentos=alimentos)


def _commit():
    '''Faz o commit ou rollback das transações de banco'''
    try:
        db.session.commit()
        return 'Cadastrado efetuado com sucesso.'
    except IntegrityError as e:
        db.session.rollback()
        error = str(e.orig)
        if 'UNIQUE constraint failed' in error:
            return f"Já existe {e.params[0]} cadastrado(a)."


@app.route('/apaga_alimento/<id>')
@login_required
def apaga_alimento(id):
    '''Apaga o alimento'''
    alimento = Alimento.query.get(id)
    db.session.delete(alimento)
    db.session.commit()
    return redirect(url_for('addalimento'))


@app.route('/apaga_tipo/<id>')
@login_required
def apaga_tipo(id):
    '''Apaga o tipo e seus relacionamentos'''
    alimentos = Alimento.query.all()
    for alimento in alimentos:
        if alimento.tipo.id == int(id):
            alimento = Alimento.query.get(alimento.id)
            db.session.delete(alimento)
    tipo = Tipo.query.get(int(id))
    db.session.delete(tipo)
    db.session.commit()
    return redirect(url_for('addtipo'))


@app.route('/logon', methods=['GET', 'POST'])
def logon():
    '''Efetua a autenticação e validação do usuário'''
    form = UserLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Acesso negado.')
            return redirect(url_for('logon'))
        login_user(user)
        flash('Acesso liberado.')
        # Medidas de segurança para não forjar acesso
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('logon.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/registro', methods=['GET', 'POST'])
@login_required
def registro():
    '''Registro de usuário'''
    form = RegistroUsuarioForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
            fullname=form.fullname.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Usuário {form.username.data} cadastrado")
        return redirect(url_for('registro'))
    return render_template('registro.html', form=form)


@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    '''Editar o perfil do usuário'''
    form = PerfilForm()
    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        user.fullname = form.fullname.data
        db.session.add(user)
        db.session.commit()
        flash('Dados atualizados')
        return redirect(url_for('perfil'))
    form.fullname.data = current_user.fullname
    return render_template('perfil.html', form=form)
