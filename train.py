import numpy as np
import pandas as pd
import sys
import os
from predict import estimate_price

data_path = "data.csv"

def get_data():
	if (not os.path.exists(data_path)):
		sys.exit("data file not found")
	try:
		return (pd.read_csv(data_path).to_numpy())
	except IOError:
		print("could not read data file")

def normalize(data):
	return ((data - np.mean(data)) / np.std(data))

def denormalize(data, ref_data):
	return ((data*np.mean(ref_data) + np.mean(ref_data)))

def compute_tetas(data, learning_rate):
	t0 = 0
	t1 = 0
	m = len(data[0])
	for j in range(0, 200):
		tmp_t0 = 0
		tmp_t1 = 0
		for i in range(0, m):
			tmp_t0 += (estimate_price(t0, t1, data[0][i]) - data[1][i])
			tmp_t1 += ((estimate_price(t0, t1, (data[0][i])) - data[1][i]) * data[0][i])
		t0 -= (tmp_t0 * learning_rate) / m
		t1 -= (tmp_t1 * learning_rate) / m
	return t0, t1

data = get_data()
normalized_data = (np.array([normalize(data[:,0]), normalize(data[:,1])]))
t0, t1 = compute_tetas(normalized_data, 0.3)
print(t0, t1)