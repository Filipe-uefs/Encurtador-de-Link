import string
from random import choice


def generator_index():

	values = string.ascii_letters + string.digits
	index = ""
	for i in range(5):
	  index += choice(values)
	return index

