import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt


def bessel_function(n, x):
    sum = 0
    for m in range(80):
        sum += (-1)**m * (x / 2)**(2 * m + n) / \
            (gamma(m + 1) * gamma(m + n + 1))
    return sum


x = np.arange(0.1, 20, 0.1)
j0 = bessel_function(0, x)
j1 = bessel_function(1, x)

fig, ax = plt.subplots()
ax.plot(x, j0, x, j1)
plt.show()
