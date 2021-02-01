from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400
