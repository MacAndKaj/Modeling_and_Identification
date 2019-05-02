import random
from math import atan

from scipy import stats
from scipy.stats import cauchy
import numpy
from matplotlib import pyplot
from numpy.ma import arange
import pylab

from Lab5_12 import K_epanechnikov, K_cosine, K_gauss


class System(object):

    def __init__(self, a=1) -> None:
        super().__init__()
        self._a = a

    def m(self, x):
        return atan(self._a * x)


def K_boxcar(x):
    if abs(x) <= 1:
        return 0.5
    else:
        return 0


def m_N(T, X, h=0.9, kernel=K_boxcar):
    estymator = []
    for x in X:
        sum_up = 0
        sum_down = 0
        for (x_n, y_n) in T:
            sum_up += y_n * kernel((x_n - x) / h)
            sum_down += kernel((x_n - x) / h)
        estymator.append(sum_up / sum_down)
    return estymator


if __name__ == '__main__':
    Q = 100
    a = [1, 10, 50, 100]
    # a = [1]

    fig = pyplot.figure(1)
    ax1 = fig.add_subplot(221)
    ax1.title.set_text("a=1")
    ax2 = fig.add_subplot(222)
    ax2.title.set_text("a=10")
    ax3 = fig.add_subplot(223)
    ax3.title.set_text("a=50")
    ax4 = fig.add_subplot(224)
    ax4.title.set_text("a=100")
    for i in range(len(a)):
        N = 1000
        uniform_a = -2
        uniform_b = 2

        normal_mu = 0
        normal_sigma = 1

        system = System(a[i])

        X = [random.uniform(uniform_a, uniform_b) for _ in range(N)]
        Z = stats.cauchy.rvs(loc=0, scale=0.01, size=N)
        # Z = [random.gauss(0, 0.5) for _ in range(N)]
        Y = [system.m(X[n]) + Z[n] for n in range(N)]
        T = [(X[n], Y[n]) for n in range(N)]
        h = 0.1
        # h = [0.1, 0.5, 1, 1.5]
        kernels = [K_boxcar, K_epanechnikov, K_cosine, K_gauss]
        # for k in range(len(h)):
        pyplot.subplot(2, 2, i + 1)

        pyplot.plot(X, m_N(T, X, h, kernels[3]), 'r.', label='$m_{N}(x)$')
        pyplot.plot(X, [system.m(x) for x in X], 'g.', label='Charakterystyka systemu')
        pyplot.legend()
        # pyplot.figure(2)
        # pylab.plot(X, Y, 'b.', label='Pomiary')
    pyplot.show()
