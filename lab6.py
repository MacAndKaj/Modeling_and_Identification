import random
from math import atan

from scipy import stats
from scipy.stats import cauchy
import numpy
from matplotlib import pyplot
from numpy.ma import arange
import pylab


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


N = 500
uniform_a = -2
uniform_b = 2


normal_mu = 0
normal_sigma = 1



def m_N(X, h=0.9):
    estymator = []
    for x in X:
        sum_up = 0
        sum_down = 0
        for (x_n, y_n) in T:
            sum_up += y_n * K_boxcar((x_n - x) / h)
            sum_down += K_boxcar((x_n - x) / h)
        estymator.append(sum_up / sum_down)
    return estymator


Q = 100

a = [1,10]
for i in range(len(a)):

    system = System(a[i])
    X = [random.uniform(uniform_a, uniform_b) for _ in range(N)]
    Z = stats.cauchy.rvs(loc=0, scale=0.01, size=N)
    Y = [system.m(X[n]) + Z[n] for n in range(N)]
    T = [(X[n], Y[n]) for n in range(N)]

    valid_h = []
    h = arange(0.1, 2, 0.01)
    for _h in h:
        sum_q = 0
        for q in range(-Q, Q, 1):
            sum_q += (m_N([q / Q], _h)[0] - system.m(q / Q)) ** 2

        valid_h.append(sum_q / (2 * Q))


    min_h = h[valid_h.index(min(valid_h))]

    pylab.figure(i+1)
    pylab.plot(X, m_N(X, min_h), 'r.', label='$m_{N}(x)$')
    pylab.plot(X, [system.m(x) for x in X], 'g.', label='m(x)')

pylab.show()