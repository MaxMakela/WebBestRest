from flask import Flask
from flask import render_template, redirect
from flask import request
from mapsJson import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['GET'])
def results():
    if 'next_page_id' in request.values and 'plc'in request.values:
        return get_rest_list(gmaps, request.values['plc'], request.values['next_page_id'])
    elif 'plc'in request.values:
        return get_rest_list(gmaps, request.values['plc'])
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
