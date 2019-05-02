from math import sqrt, pi, cos

import numpy
from matplotlib import pyplot
import random

import Lab1
import Lab2
import Lab4b


def K_boxcar(x):
    if abs(x) <= 1:
        return 0.5
    else:
        return 0


def K_gauss(x):
    return (1 / sqrt(2 * numpy.pi)) * numpy.exp(-(x ** 2) / 2)


def K_epanechnikov(x):
    if abs(x) <= 1:
        return 0.75 * (1 - x ** 2)
    else:
        return 0


def K_tricube(x):
    if abs(x) <= 1:
        return (70 / 81) * (1 - abs(x) ** 3) ** 3
    else:
        return 0



def K_cosine(x):
    if abs(x) <= 1:
        return pi*cos(pi*x/2)/4
    else:
        return 0


def gauss_func(x, mu, sigma):
    return numpy.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / sqrt(2 * numpy.pi * sigma ** 2)


def kernel_estimator(X_numbers, x, h, kernel_function=K_boxcar):
    arr = [kernel_function((x_n - x) / h) for x_n in X_numbers]
    return sum(arr) / (len(X_numbers) * h)


if __name__ == '__main__':
    N = 500
    uniform = [random.uniform(0, 1) for _ in range(N)]
    X = Lab1.Generator().generate_random_numbers(uniform,Lab1.Ex2())
    space = numpy.arange(-3, 5, 0.01)
    normal = [Lab2.Ex1().f(x) for x in space]
    fig = pyplot.figure(1)
    ax1 = fig.add_subplot(321)
    ax2 = fig.add_subplot(322)
    ax3 = fig.add_subplot(323)
    ax4 = fig.add_subplot(324)
    ax5 = fig.add_subplot(325)
    ax6 = fig.add_subplot(326)

    # h_list = [0.01] + [round(h,2) for h in numpy.arange(0.25, 1.26, 0.25)]
    h_list = [0.11]
    for h in h_list:
        # pyplot.subplot(3, 2, 1 + h_list.index(h))

        f_n_boxcar = [kernel_estimator(X, x, h, K_boxcar) for x in space]
        f_n_cosine = [kernel_estimator(X, x, h, K_cosine) for x in space]
        f_n_gauss = [kernel_estimator(X, x, h, K_gauss) for x in space]
        f_n_epanechnikov = [kernel_estimator(X, x, h, K_epanechnikov) for x in space]
        # f_n_tricube = [kernel_estimator(X, x, h, K_tricube) for x in space]


        fig = pyplot.figure(1)
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)
        ax4.title.set_text("Boxcar")
        ax1.title.set_text("Cosine")
        ax2.title.set_text("Gaussian")
        ax3.title.set_text("Epanechnikov")
        # ax4.title.set_text("Tricube")

        pyplot.subplot(2, 2, 1)
        # pyplot.plot(space, f_n_boxcar)
        pyplot.plot(space, f_n_cosine)
        pyplot.plot(space, normal)
        pyplot.legend()
        pyplot.subplot(2, 2, 2)
        pyplot.plot(space, f_n_gauss)
        pyplot.plot(space, normal)
        pyplot.subplot(2, 2, 3)
        pyplot.plot(space, f_n_epanechnikov)
        pyplot.plot(space, normal)
        pyplot.subplot(2, 2, 4)
        # pyplot.plot(space, f_n_tricube)
        pyplot.plot(space, f_n_boxcar)
        pyplot.plot(space, normal)

    pyplot.show()

# for k in [N * i for i in range(1, 6)]:
#     estymator = []
#     random_numbers = []
#
#     for _ in range(k):
#         random_numbers.append(random.gauss(1, 1))
#
#     f_n_list = []
#     gauss_list = []
#
#     przedzial = numpy.arange(-2, 3, 0.001)
#     for h in h_list:
#         estymator = []
#         for x in przedzial:
#             suma = 0
#             for val in random_numbers:
#                 suma += K_boxcar((val - x) / h)
#             estymator.append(suma / (k * h))
#
#         f_n_list.append(estymator)
#
#     for x in przedzial:
#         gauss_list.append(gauss_func(x, 1, 1))
#
#     labels = []
#     i = 0
#     plt.figure(int(k / N))
#     for f in f_n_list:
#         plt.plot(przedzial, f)
#         labels.append('h=' + str(h_list[i]))
#         i += 1
#     plt.legend(labels)
#     plt.plot(przedzial, gauss_list)
#     print("zrobione")
#
# plt.show()
