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

# def lista_tipos(request, id):
#     tipo = Tipo.query.get(id)
#     form = AlimentoForm(request.POST, obj=tipo)
#     form.tipos.choices = [(t.id, t.name) for t in Tipo.query.order_by('tipo')]
