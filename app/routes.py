'''
route URLs implemented by the application

'''

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
	user = {'username' : 'Vihar'}
	dropdown = ["SPY", "DIA", "MSFT"]
	return render_template('index.html', title='Stock App on AWS', user=user, dropdown = dropdown)