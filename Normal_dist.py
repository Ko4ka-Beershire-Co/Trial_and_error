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

x = np.random.normal(mu, sigma, n)
y = normal(X, mu, sigma)

print(X)
print(x)
print(y)

fig = plt.scatter(x=X, y=y)
fig.show()
