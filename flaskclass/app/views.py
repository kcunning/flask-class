from app import app

@app.route('/')
def lucky_static():
	return "Your lucky number is 7"
