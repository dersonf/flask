from app import app
from app.forms import AutoCompleteForm
from flask import render_template, request, jsonify

NAMES = ["anderson", "patricia", "jascira", "andre", "pamela"]

@app.route('/')
def index():
    form = AutoCompleteForm()
    return render_template('index.html', form=form)


@app.route('/autocomplete',methods=['GET'])
def autocomplete():
    search = request.args.get('term')

    app.logger.debug(search)
    return jsonify(json_list=NAMES)