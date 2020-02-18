import numpy as np
import pandas as pd
import sys
import os
#from predict import estimate_price

data_path = "data.csv"

def get_data():
	if (not os.path.exists(data_path)):
		sys.exit("data file not found")
	try:
		return (pd.read_csv(data_path).to_numpy())
	except IOError:
		print("could not read data file")

def normalize_column(column):
	return ((column - np.mean(column)) / np.std(column))

data = get_data()
normalized_data = (np.array([normalize_column(data[:,0]), normalize_column(data[:,1])]))

print(normalized_data)