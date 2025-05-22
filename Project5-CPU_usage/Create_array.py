# Create a 3D array that simulates 7 days of hourly CPU usage data from 5 servers (shape: 7 x 24 x 5), filled with random integers from 5 to 95%.

import numpy as np

cpu_usage_data = np.random.randint(5, 96, size=(7, 24, 5))


# np.random is a module inside numpy that contains many functions to generate random numbers
# It is used when you want to simulate randomness in your data, like
# Random Integers
# Random floating-point numbers
# Random samples from distributions
# Random shuffling, stc

# randint:
# np.random.randint(low, high=None, size=None) generates random integers.
# It returns random integers between low(inclusive) and high(exclusive)
# If only one parameter is given, it is treated as the upper bound and low defaults to 0.
# [low, high) - 2 arguments
# size - shape of an output array

