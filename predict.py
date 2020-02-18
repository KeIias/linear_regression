import sys
import os

f_teta = "teta_values"

def is_float(value):
	try:
		float(value)
		if (value.isalpha()):
			return False
		return True
	except ValueError:
		return False

def get_teta_values():
	if os.path.exists(f_teta):
		try:
			file = open(f_teta, "r")
			l1 = file.readline().strip()
			l2 = file.readline().strip()
			if (is_float(l1) and is_float(l2)):
				return(float(l1), float(l2))
			else:
				sys.exit("file content is not a number or not enough lines were provided")
		except IOError:
			print("could not read file")
	else:
		sys.exit(str.format("no file called " + f_teta))

def estimate_price(mileage):
	t0, t1 = get_teta_values()
	return (t0 + (t1*mileage))

while (True):
	print('Type prediction to make:')
	user_input = input()
	if (is_float(user_input)):
		print("Predicted value:")
		print(estimate_price(user_input))
		sys.exit(0)
	else:
		print("Invalid input")