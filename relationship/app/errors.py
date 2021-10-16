from app import app
from flask import render_template


@app.errorhandler(404)
def not_found_error(error):
    '''Erro 404'''
    return render_template('404.html'), 404
