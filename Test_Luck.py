# When I forget the math behind this shit: MU( utorrent letter) = mode, median; SIGMA( apple) = standard dev


import numpy as np
import plotly.express as plt
import scipy.stats as stats

mu, sigma, n = 50, 25, 1000
lower, upper = 0, 100


def normal(x, mu, sigma):
    return (2. * np.pi * sigma ** 2.) ** -.5 * np.exp(-.5 * (x - mu) ** 2. / sigma ** 2.)


X = stats.truncnorm.rvs(
    (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=n)

# Visual
# x = np.random.normal(mu, sigma, n)
Y = normal(X, mu, sigma)

fig = plt.scatter(x=X, y=Y)
fig.show()

# Part 2: Luck

# X = X - 10
X = X * 0.9

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


# Hashmap or !turtle!

def turtle(range1, range2):
    i = 0
    j = 0
    found = 0
    while i < len(range1) and j < len(range2):
        if range1[i] == range2[j]:
            found = found + 1
            i = i + 1
            j = j + 1
        elif range1[i] < range2[j]:
            i = i + 1
        else:
            j = j + 1
    return found


print(turtle(sorted(Array_indices), sorted(X_indices)))
