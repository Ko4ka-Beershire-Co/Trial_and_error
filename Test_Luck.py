# When I forget the math behind this shit: MU( utorrent letter) = mode, median; SIGMA( apple) = standard dev


import numpy as np
import plotly.express as plt
import scipy.stats as stats

mu, sigma, n = 50, 20, 1000
lower, upper = 0, 100


def normal(x, mu, sigma):
    return (2. * np.pi * sigma ** 2.) ** -.5 * np.exp(-.5 * (x - mu) ** 2. / sigma ** 2.)


X = stats.truncnorm.rvs(
    (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=n)

# x = np.random.normal(mu, sigma, n)
Y = normal(X, mu, sigma)

# Part 2: Luck

Z = np.random.random_integers(1, 10, n)

Array = X + Z

# Check-up
# T = np. count_nonzero(Array)
# print(T)

top = 10
Array_indices = (-Array).argsort()[:top]
print(sorted(Array_indices))

X_indices = (-X).argsort()[:top]
print(sorted(X_indices))

# Hashmap or turtle
