import os
# Envio de erros para o e-mail
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
# Esse é o modulo app
from flask import Flask
# Esse modulo é localizado na pasta que antecede app, a pasta root
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Implementa a administração de autenticação do usuário
from flask_login import LoginManager
# Modulo do Flask Mail
from flask_mail import Mail

app = Flask(__name__)
# Carrega todas as configs da classe Config
app.config.from_object(Config)
# Instacia o modulo de banco de dados
db = SQLAlchemy(app)
# Instancia o modulo de atualização do banco de dados
migrate = Migrate(app, db)
# Instancia o modulo de gerenciamento de sessão/autenticação do usuário
login = LoginManager(app)
# Instancia o Flask Mail
mail = Mail(app)
# Definindo a view onde o usuário efetua login quando for obrigatório
# com @login_required
login.login_view = 'login'

# models é a estrutura do banco de dados
from app import routes, models, errors

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # Gravando os erros em arquivos de log
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

