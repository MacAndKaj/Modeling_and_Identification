from math import sqrt

import numpy
from matplotlib import pyplot as plt
import random

h_list = numpy.arange(1, 0.01, -0.25)
N = 1000


def K_boxcar(x):
    if abs(x) <= 1:
        return 0.5
    else:
        return 0


def K_gauss(x):
    return (1 / sqrt(2 * numpy.pi)) * numpy.exp(-(x ** 2) / 2)


def gauss_func(x, mu, sigma):
    return numpy.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / sqrt(2 * numpy.pi * sigma ** 2)


for k in [N * i for i in range(1,6)]:
    estymator = []
    random_numbers = []

    for _ in range(k):
        random_numbers.append(random.gauss(1, 1))

    f_n_list = []
    gauss_list = []

    przedzial = numpy.arange(-2, 3, 0.001)
    for h in h_list:
        estymator = []
        for x in przedzial:
            suma = 0
            for val in random_numbers:
                suma += K_boxcar((val - x) / h)
            estymator.append(suma / (k * h))

        f_n_list.append(estymator)

    for x in przedzial:
        gauss_list.append(gauss_func(x, 1, 1))

    labels = []
    i = 0
    plt.figure(int(k/N))
    for f in f_n_list:
        plt.plot(przedzial, f)
        labels.append('h=' + str(h_list[i]))
        i += 1
    plt.legend(labels)
    plt.plot(przedzial, gauss_list)
    print("zrobione")

plt.show()
