# Esse é o modulo app
from flask import Flask
# Esse modulo é localizado na pasta que antecede app, a pasta root
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Implementa a administração de autenticação do usuário
from flask_login import LoginManager

app = Flask(__name__)
# Carrega todas as configs da classe Config
app.config.from_object(Config)
# Instacia o modulo de banco de dados
db = SQLAlchemy(app)
# Instancia o modulo de atualização do banco de dados
migrate = Migrate(app, db)
# Instancia o modulo de gerenciamento de sessão/autenticação do usuário
login = LoginManager(app)
# Definindo a view onde o usuário efetua login quando for obrigatório
# com @login_required
login.login_view = 'login'

# models é a estrutura do banco de dados
from app import routes, models
