import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'relationship.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or '&rOq_/]CKyK&H8Lw8$'
