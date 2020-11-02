# When I forget the math behind this shit: MU( utorrent letter) = mode, median; SIGMA( apple) = standard dev


import numpy as np
import plotly.express as plt

mu, sigma, n = 50, 20, 1000


def normal(x, mu, sigma):
    return (2. * np.pi * sigma ** 2.) ** -.5 * np.exp(-.5 * (x - mu) ** 2. / sigma ** 2.)


x = np.random.normal(mu, sigma, n)
y = normal(x, mu, sigma)

# print(x)
# print(y)

fig = plt.scatter(x=x, y=y)
fig.show()
