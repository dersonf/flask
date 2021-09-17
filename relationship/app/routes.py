from flask.helpers import url_for
from app import app, db
from flask import render_template, redirect
from app.models import Alimento, Tipo
from app.forms import TipoForm, AlimentoForm


@app.route('/')
def index():
    vegetais = Alimento.query.all()
    return render_template('index.html', vegetais=vegetais)


@app.route('/addtipo', methods=['GET', 'POST'])
def addtipo():
    '''Adiciona o tipo de vegetal'''
    form = TipoForm()
    tipos = Tipo.query.all()
    if form.validate_on_submit():
        tipo = Tipo(tipo=form.tipo.data)
        db.session.add(tipo)
        db.session.commit()
        return redirect(url_for('addtipo'))
    return render_template('addtipo.html', form=form, tipos=tipos)


@app.route('/addalimento', methods=['GET', 'POST'])
def addalimento():
    '''Adiciona o vegetal'''
    form = AlimentoForm()
    form.tipos.choices = [(t.id, t.tipo) for t in Tipo.query.order_by('tipo')]
    alimentos = Alimento.query.all()
    if form.validate_on_submit():
        tipo = Tipo.query.get(form.tipos.data)
        alimento = Alimento(alimento=form.alimento.data, tipo=tipo)
        db.session.add(alimento)
        db.session.commit()
        return redirect(url_for('addalimento'))
    return render_template('addalimento.html', form=form, alimentos=alimentos)


@app.route('/apaga_alimento/<id>')
def apaga_alimento(id):
    '''Apaga o alimento'''
    alimento = Alimento.query.get(id)
    db.session.delete(alimento)
    db.session.commit()
    return redirect(url_for('addalimento'))


@app.route('/apaga_tipo/<id>')
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