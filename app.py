from flask import Flask
from flask import render_template, redirect
from flask import request
from mapsJson import get_rest_list, gmaps


application = Flask(__name__)


@application.route('/')
def home():
    return render_template('home.html')


@application.route('/results', methods=['GET'])
def results():
    if 'plc' in request.values:
        return get_rest_list(gmaps, request.values['plc'], request.values.get("next_page_id"))
    else:
        return redirect('/')


if __name__ == '__main__':
    application.run(debug=True)
