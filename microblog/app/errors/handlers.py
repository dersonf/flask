from flask import render_template
from app import db
from app.errors import bp


@app.errorhandler(404)
def not_found_error(error):
    'Tela customizada para o erro 404'
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    'Tela customizada para o erro 500'
    db.session.rollback()
    return render_template('500.html'), 500
