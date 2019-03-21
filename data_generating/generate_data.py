
import matplotlib.pyplot as plt
import random
import numpy as np

samples = np.random.normal(0, 1, size=5000)

#Add trend to data
trend_samples = []
for count, sample in enumerate(samples):

	point = abs(sample)+0.05*count**1.5
	point = point + np.sin(count/100)*500
	trend_samples.append(point)


plt.plot(samples)

# plt.plot(trend_samples)



plt.show()