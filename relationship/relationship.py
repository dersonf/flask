from app import app, db
from app.models import Tipo, Alimento, User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Tipo': Tipo, 'Alimento': Alimento, 'User': User}
