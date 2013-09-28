from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class GetLucky(Form):
	numbers = TextField('numbers')

	def validate(self):
		nums = self.numbers.data.split()
		valid = True
		for num in nums:
			if not num.isdigit():
				valid = False
		if len(nums) != 3:
			valid = False

		return valid
