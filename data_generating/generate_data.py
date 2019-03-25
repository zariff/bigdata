
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
import csv

start_value = 5
start_time_shift =20
random_walk_weight = 0.01
random_walk_variance = 1
seasonality_1_freq = 50 #lower is shorter
seasonality_1_weight = 5
seasonality_2_freq = 7 #lower is shorter
seasonality_2_weight = 2

sample_size = 1000

trend = 0.02
exponent = 1
codes = list('abcdefghijklmnopqrstuvwxyz')
n_samples = 10

terms = []
with open('wordlist.csv', 'r') as f:
	reader = csv.reader(f)
	terms = [word[0] for word in list(reader)]
	random.shuffle(terms)

# Generates time series
def generate_ts():
	sample = []
	random_walk = np.random.normal(0,random_walk_variance)
	y = start_value

	for time in np.arange(sample_size):

		#Assume no start at y = 0
		time = time + start_time_shift

		#Add seasonality 1
		y = (np.sin(time/seasonality_1_freq))*seasonality_1_weight
		

		#Add seasonality 2
		y = y + np.sin(time/seasonality_2_freq)*seasonality_2_weight

		#Add trend
		y = y + (trend * (time ** exponent))

		# Random walk component
		random_walk = random_walk + np.random.normal(0,random_walk_variance)
		y = y + random_walk * random_walk_weight
		

		sample.append(max(0, y))
	return sample

#Plot some time series
def plot_ts(n):
	for _ in range(n):
		plt.plot(generate_ts())

#Creates a dummy dataset from n time series for 'codes'

#For profiling by line:
#kernprof -l generate_data.py
#python3 -m line_profiler generate_data.py.lprof
@profile 
def create_dummy_dataset():
	df = []
	sample_range = 0
	for i in range(n_samples):
		sample = generate_ts()
		for index, number in enumerate(sample): #Loop over a sample
			for n in range(int(round(number))): #Create n entries
				date = datetime.datetime(2000, 1, 1, 0, 0) + timedelta(days=index)
				current_sample = i+index+n
				sample = terms[current_sample:current_sample+100]
				text = " ".join(sample)
				df.append([date, codes[i], text])
	pandas_df = pd.DataFrame(df, columns=['date', 'code', 'text'])
	return pandas_df


dummy_dataset = create_dummy_dataset()
print(dummy_dataset)

# plot_ts(10)
# plt.show()