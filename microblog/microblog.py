from app import app, db
from app.models import User, Post


# Esse decorator carrega a base e as tabelas no flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
