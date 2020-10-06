import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from predict import estimate_price

data_path = "data.csv"

def get_data():
	if (not os.path.exists(data_path)):
		sys.exit("data file not found")
	try:
		return (pd.read_csv(data_path))
	except:
		print("could not read data file")

def reshape_data(data):
	return (np.array([data[:,0], data[:,1]]))

def standardize(data):
	return (data - np.mean(data)) / np.std(data)

def unstandardize(data, ref_data):
	return data * np.std(ref_data) + np.mean(ref_data)

def unstandardize_theta(theta, data):
	x = data[0]
	y = estimate_price(theta[0], theta[1], standardize(x))
	y = unstandardize(y, data[1])
	
	ax1.plot(x, y)
	last = len(x) - 1
	a = (y[last] - y[0]) / (x[last] - x[0])
	b = y[0] - (x[0] * a)
	theta = (b, a)
	return theta

def compute_theta(x, y, learning_rate):
	m = len(x)
	theta = np.zeros(2)
	error_history = []

	for j in range(0, epochs):
		tmp_theta = np.zeros(2)
		iteration_error = 0
		for i in range(0, m):
			prediction = estimate_price(theta[0], theta[1], x[i])
			error = prediction - y[i]
			tmp_theta[0] += error
			tmp_theta[1] += error * x[i]
			#Equivalent to the 4 lines above, I just broke down the formula for readability purposes
			#tmp_theta[0] += (estimate_price(theta[0], theta[1], x[i]) - y[i])
			#tmp_theta[1] += (estimate_price(theta[0], theta[1], x[i]) - y[i]) * x[i]
			iteration_error += error**2
		iteration_error /= m
		error_history.append(iteration_error)
		theta -= (tmp_theta * learning_rate) / m
	ax2.set_xlabel("Iterations", fontsize=21)
	ax2.set_ylabel("Error", fontsize=21)
	ax2.plot(list(range(0, len(error_history))), error_history)
	return theta

epochs = 100

if (__name__ == "__main__"):
	data = get_data()
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18,8))

	ax1.set_xlabel(data.columns[0], fontsize=21)
	ax1.set_ylabel(data.columns[1], fontsize=21)
	data = reshape_data(data.to_numpy())
	ax1.plot(data[0], data[1], "+", color="red")
	theta = compute_theta(standardize(data[0]), standardize(data[1]), 0.1)
	theta = unstandardize_theta(theta, data)
	plt.show()
	try:
		np.savetxt("theta_values", theta, fmt="%.20f")
		print("Coefficients successfully computed and saved in theta_values")
	except:
		print("Could not save coefficients in theta_values file")