import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'K0luJruv4O}5c4S'
