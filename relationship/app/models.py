from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Relacionamento de um pra muitos onde o tipo é um e alimento é muitos
class Tipo(db.Model):
    '''Tabela de tipo de alimento'''
    id = db.Column(db.Integer, unique=True, primary_key=True)
    tipo = db.Column(db.String(20), unique=True, nullable=False)
    # esse campo alimentos é uma view
    # lazy é como a view vai se comportar, 'dynamic' precisa dos filtros
    # dynamic é bom quando há muitos itens e True acaba deixando a aplicação
    # lenta porque tras all() sempre
    # backref é adicionado na tabela alimento que foi declarado no início
    alimentos = db.relationship('Alimento', backref='tipo', lazy=True)

    def __repr__(self):
        '''
        Função pra troubleshooting, quando é chamado a instância vem esse valor
        '''
        return f"<Tipo: {self.tipo}>"


class Alimento(db.Model):
    '''Tabela de alimento'''
    id = db.Column(db.Integer, unique=True, primary_key=True)
    alimento = db.Column(db.String(40), unique=True, nullable=False)
    # O relacionamento da chave estrangeira refere-se a tabela tipo campo id
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)

    def __repr__(self):
        return f"<Alimento: {self.alimento}>"


class User(UserMixin, db.Model):
    '''Armazena os dados dos usuários e carrega metodos de autenticação'''
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    fullname = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return f"<Username: {self.username}>"

    def set_password(self, password):
        '''Define a hash da senha'''
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


'''
referencias:
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

# Adicionando os tipos
t1 = Tipo(tipo='fruta')
t2 = Tipo(tipo='tuberculo')
t3 = Tipo(tipo='verdura')

db.session.add_all([t1, t2, t3])
db.session.commit()

tipos = Tipo.query.all()

for tipo in tipos:
    print(tipo.id, tipo.tipo)

# Adicionando os alimentos, note que utilizamos o backref de tipo pra 
atribuir a chave estrangeira, tipo é um campo virtual
a1 = Alimento(alimento='banana', tipo=t1)
a2 = Alimento(alimento='maça', tipo=t1)
a3 = Alimento(alimento='batata', tipo=t2)
a4 = Alimento(alimento='mandioca', tipo=t2)
a5 = Alimento(alimento='acelga', tipo=t3)
a6 = Alimento(alimento='alface', tipo=t3)
a7 = Alimento(alimento='repolho', tipo=t3)

db.session.add_all([a1, a2, a3, a4, a5, a6, a7])
db.session.commit()

alimentos = Alimento.query.all()

for alimento in alimentos:
    print(alimento.id, alimento.alimento)

# Fazendo as queries
alimentos = Alimento.query.all()

for a in alimentos:
    print(a.id, a.alimento, a.tipo.tipo)
'''