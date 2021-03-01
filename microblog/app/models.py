from datetime import datetime
from app import db


class User(db.Model):
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


class Post(db.Model):
    'Classe que cria a tabela dos posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # Chave estrangeira que relaciona o usuário ao post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "f<Post {self.body}>"
