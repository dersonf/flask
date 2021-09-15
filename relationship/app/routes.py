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
    alimentos = Alimento.query.all()
    return render_template('addalimento.html', form=form, alimentos=alimentos)
