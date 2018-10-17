from flask import Flask
from flask import render_template
from flask import request
from mapsJson import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['GET'])
def results():
    if request.method == 'GET' and request.values['plc']:
        best_rests = set_best_rest_list(gmaps, request.values['plc'])
        return render_template('home.html', rest_list=best_rests)
    else:
        return render_template('home.html')

#
# @app.route('/search_rest', methods=['POST', 'GET'])
# def get_rest():
#     return get_rest_list(gmaps, request.values['plc'])


if __name__ == '__main__':
    app.run(debug=True)
