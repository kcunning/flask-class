from app import app
from flask import render_template

from forms import GetLucky

from random import randint

@app.route('/')
def lucky_static():
	lucky_num = randint(1, 10)
	return render_template('simple.html', lucky_num=lucky_num)

@app.route('/<max>/')
def lucky_max(max):
	lucky_num = randint(1, int(max))
	return render_template('simple.html', lucky_num=lucky_num)

@app.route('/game/')
def game():
	game_nums = []
	while len(game_nums) < 5:
		n = randint(1, 10)
		if not n in game_nums:
			game_nums.append(n)
	return render_template('game.html', game_nums = game_nums)

@app.route('/nums/', methods=['GET', 'POST'])
def get_nums():
	form = GetLucky()
	return render_template('get_lucky.html', form=form)
