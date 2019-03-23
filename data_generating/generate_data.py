
import matplotlib.pyplot as plt
import random
import numpy as np

sample_size = 5000
random_walk_weight = 10
random_walk_variance = 10
trend = 0.2
exponent = 1.2


# Get index for time series

def generate_ts():
	index = np.arange(sample_size)
	sample = []
	random_walk = np.random.normal(0,random_walk_variance)

	for time in index:

		#Add seasonality 1
		y = np.sin(time/100)*200

		#Add seasonality 2
		y = y + np.sin(time/250)*400

		#Add trend
		y = y + (trend * time ** exponent)

		# Random walk component
		random_walk = random_walk + np.random.normal(0,random_walk_variance)
		y = y + random_walk * random_walk_weight
		

		sample.append(y)
	return sample

def plot_ts(n):
	for _ in range(n):
		plt.plot(generate_ts())



plot_ts(10)

plt.show()