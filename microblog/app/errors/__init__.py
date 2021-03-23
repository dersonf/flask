from flask import Blueprint

bp = Blueprint('errors', __name__)

# É feito no fim para evitar dependencias circulares
from app.errors import handlers