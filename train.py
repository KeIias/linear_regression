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
		return (pd.read_csv(data_path).to_numpy())
	except IOError:
		print("could not read data file")

def standardize(data):
	return ((data - np.mean(data)) / np.std(data))

def unstandardize(data, ref_data):
	return ((data*np.mean(ref_data) + np.mean(ref_data)))

def compute_theta(x, y, learning_rate):
	m = len(x)
	theta = np.zeros(2)
	for j in range(0, 200):
		tmp_theta = np.zeros(2)
		for i in range(0, m):
			prediction = estimate_price(theta[0], theta[1], x[i])
			error = prediction - y[i]
			tmp_theta[0] += error
			tmp_theta[1] += error * x[i]
			#Equivalent to the 4 lines above, I just broke down the formula for readability purposes
			#tmp_theta[0] += (estimate_price(theta[0], theta[1], x[i]) - y[i])
			#tmp_theta[1] += (estimate_price(theta[0], theta[1], x[i]) - y[i]) * x[i]
		theta -= (tmp_theta * learning_rate) / m
	return theta

data = get_data()
standardized_data = (np.array([standardize(data[:,0]), standardize(data[:,1])]))
theta = compute_theta(standardized_data[0], standardized_data[1], 0.3)
print(theta)