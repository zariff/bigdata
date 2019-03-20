import TimeSynth.timesynth as ts
import matplotlib.pyplot as plt
import random
import numpy as np

time_sampler = ts.TimeSampler(stop_time=20)
# Sampling irregular time samples
irregular_time_samples = time_sampler.sample_irregular_time(num_points=5000, keep_percentage=50)


# Initializing Sinusoidal signal
sinusoid = ts.signals.Sinusoidal(frequency=0.1)
# Initializing Gaussian noise
white_noise = ts.noise.GaussianNoise(std=100)
# Initializing TimeSeries class with the signal and noise objects
timeseries = ts.TimeSeries(sinusoid, noise_generator=white_noise)
# Sampling using the irregular time samples
samples, signals, errors = timeseries.sample(irregular_time_samples)

#Add trend to data
trend_samples = []
for count, sample in enumerate(samples):

	point = abs(sample)+0.05*count**1.5
	point = point + np.sin(count/100)*500
	trend_samples.append(point)


plt.plot(samples)
plt.plot(irregular_time_samples)
plt.plot(trend_samples)



plt.show()