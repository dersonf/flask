import os
# Envio de erros para o e-mail
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
# Esse é o modulo app
from flask import Flask, request
# Esse modulo é localizado na pasta que antecede app, a pasta root
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Implementa a administração de autenticação do usuário
from flask_login import LoginManager
# Modulo do Flask Mail
from flask_mail import Mail
# Modulo do Bootstrap - pra deixar mais bunitim
from flask_bootstrap import Bootstrap
# Modulo para coletar e imprimir a data e hora de acordo com o SO do usuário
from flask_moment import Moment
# Modulo para a tradução do blog
from flask_babel import Babel
# Importando o blueprint de erros
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

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
# Instanciando o Bootstrap
bootstrap = Bootstrap(app)
# Instanciando o modulo de data e hora
moment = Moment(app)
# Instaciando o modulo de tradução do Babel
babel = Babel(app)

# Definindo a view onde o usuário efetua login quando for obrigatório
# com @login_required
login.login_view = 'login'
# Personalizando a mensagem de login obrigatório.
login.login_message = 'Se não estiver autenticado já era.'

# Decorator pra pegar a linguagem a ser traduzida
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# models é a estrutura do banco de dados
# removido a função errors
from app import routes, models

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
