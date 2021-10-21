from app import app, db, login
from flask import render_template, redirect, flash, url_for
from app.models import Alimento, Tipo, User
from app.forms import (
    TipoForm,
    AlimentoForm,
    # PerfilForm,
    )
from app.tabela import ItemTable
from sqlalchemy.exc import IntegrityError
from flask_login import login_required


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    items = []
    vegetais = Alimento.query.all()
    for vegetal in vegetais:
        items.append(dict(id=vegetal.id, alimento=vegetal.alimento, vegetal=vegetal.tipo.tipo))
    tabela = ItemTable(items)
    return render_template('index.html', tabela=tabela)


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


# @app.route('/perfil', methods=['GET', 'POST'])
# @login_required
# def perfil():
#     '''Editar o perfil do usuário'''
#     form = PerfilForm()
#     if form.validate_on_submit():
#         user = User.query.get(current_user.id)
#         user.fullname = form.fullname.data
#         db.session.add(user)
#         db.session.commit()
#         flash('Dados atualizados')
#         return redirect(url_for('perfil'))
#     form.fullname.data = current_user.fullname
#     return render_template('perfil.html', form=form)
