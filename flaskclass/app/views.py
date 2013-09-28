from app import app
from flask import render_template, request

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

def get_game_nums(num=5, max=10):
	game_nums = []
	while len(game_nums) < num:
		n = randint(1, 10)
		if not n in game_nums:
			game_nums.append(n)
	return game_nums

@app.route('/game/')
def game():
	game_nums = get_game_nums()
	return render_template('game.html', game_nums = game_nums)

@app.route('/nums/', methods=['GET', 'POST'])
def get_nums():
	form = GetLucky()
	if form.validate_on_submit():
		if request.method == 'POST':
			numbers = form.numbers.data
			game_nums = get_game_nums()
			nums = numbers.split()
			wins = 0
			for num in nums:
				if int(num) in game_nums:
					wins += 1
			return render_template('game.html', game_nums=game_nums,
					player_nums=numbers, wins=wins)
	else:
		return render_template('get_lucky.html', form=form)
	if request.method == 'GET':	
		return render_template('get_lucky.html', form=form)
