import numpy as np
import matplotlib.pyplot as plt

pi = np.pi


def main():
    x = np.arange(-1 * pi, 1 * pi, pi / 50)
    s = 0
    for n in range(50):
        s += (-1)**n * np.cos((2 * n + 1) * x) / ((2 * n + 1) * pi)
    s1 = np.cos(x) / pi
    s3 = -np.cos(3 * x) / (9 * pi)
    s5 = -np.cos(5 * x) / (5 * pi)
    s0 = s1 + s5

    fig, ax = plt.subplots()
    plt.plot(x, s5, x, s0)
    plt.show()


if __name__ == '__main__':
    main()


