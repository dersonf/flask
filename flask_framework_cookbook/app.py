from flask import Flask
import configuration

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')

@app.route('/')
def hello_world():
    return 'Hello to the World Flask!'


if __name__ == '__main__':
    app.run(debug=True)
