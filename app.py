from flask import Flask
from flask import render_template
from flask import request
from mapsJson import set_best_rest_list
from mapsJson import gmaps


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search_results', methods=['POST'])
def results():
    if request.method == 'POST' and request.form['plc']:
        best_rests = set_best_rest_list(gmaps, request.form['plc'])
        return render_template('results.html', rest_list=best_rests)
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
