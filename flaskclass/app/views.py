from app import app
from flask import render_template

from random import randint

@app.route('/')
def lucky_static():
	lucky_num = randint(1, 10)
	return render_template('simple.html', lucky_num=lucky_num)

@app.route('/<max>/')
def lucky_max(max):
	lucky_num = randint(1, int(max))
	return render_template('simple.html', lucky_num=lucky_num)
