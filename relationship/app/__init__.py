# carregando modulo do sqlalchemy
from sqlalchemy import MetaData
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# criando a convensão de nomes para constraints
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# Adicionando a convensão nos metadados
metadata = MetaData(naming_convention=convention)

app = Flask(__name__)
app.config.from_object(Config)
# Carregando os metadados na instância
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)

login.login_view = 'auth.logon'
login.login_message = 'Necessário efetuar o login.'

from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp, url_prefix='/errors')

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app import models
