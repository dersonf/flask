# Esse é o modulo app
from flask import Flask
# Esse modulo é localizado na pasta que antecede app, a pasta root
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Carrega todas as configs da classe Config
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models é a estrutura do banco de dados
from app import routes, models
