import sys
import os

f_theta = "theta_values"

def is_float(value):
	try:
		float(value)
		if (value.isalpha()):
			return False
		return True
	except:
		return False

def get_teta_values():
	if os.path.exists(f_theta):
		try:
			file = open(f_theta, "r")
			l1 = file.readline().strip()
			l2 = file.readline().strip()
			if (is_float(l1) and is_float(l2)):
				return(float(l1), float(l2))
			else:
				sys.exit("file content is not a number or not enough lines were provided")
		except:
			sys.exit("could not read theta_values file")
	else:
		sys.exit(str.format("no file called " + f_theta))

def estimate_price(t0, t1, mileage):
	return (t0 + (t1 * mileage))

def main():
	while (True):
		t0, t1 = get_teta_values()
		print('Type prediction to make:')
		user_input = input()
		if (is_float(user_input)):
			print("Predicted value:")
			print(estimate_price(t0, t1, float(user_input)))
			break
		else:
			print("Invalid input")

if __name__ == "__main__":
	main()