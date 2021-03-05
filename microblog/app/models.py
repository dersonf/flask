from datetime import datetime
from hashlib import md5
# Introduz a criptografia que armazena a hash de uma palavra qualquer
from werkzeug.security import generate_password_hash, check_password_hash
# Para ajudar nos metodos do modulo flask-login
from flask_login import UserMixin
from app import db
from app import login


class User(UserMixin, db.Model):
    'Como a classe chama User a tabela terá o nome user'
    'Classe que cria a tabela de usuários'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # Isso é uma view
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Ao criar usuário ele cospe ele na saída padrão
    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        'Gera a hash a ser armazenada na base'
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        'Retorna falso ou verdadeiro na verificação da hash'
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        'Gera url para o avatar em gravatar'
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=robohash&r=x&s={size}"


class Post(db.Model):
    'Classe que cria a tabela dos posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # Chave estrangeira que relaciona o usuário ao post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.body}>"


# Para passar o id do usuário para o Flask-Login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))