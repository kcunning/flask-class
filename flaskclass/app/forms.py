from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class GetLucky(Form):
	numbers = TextField('numbers')
