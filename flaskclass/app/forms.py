from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class GetLucky(Form):
	numbers = TextField('numbers')

	def validate(self):
		nums = self.numbers.data.split()
		valid = True
		errors = []

		for num in nums:
			if not num.isdigit():
				valid = False
				errors.append('One of the items is not a number')

		if len(nums) != 3:
			valid = False
			errors.append('You may submit exactly three numbers.')

		self.numbers.errors = tuple(errors)

		return valid
