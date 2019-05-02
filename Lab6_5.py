import random

from matplotlib import pyplot
from numpy.ma import arange

from Lab5_12 import K_epanechnikov, K_cosine, K_gauss, K_boxcar
from lab6 import System, m_N


def valid_h(T, Q, h, system, kernel):
    arr = [(m_N(T, [q / Q], h, kernel)[0] - system.m(q / Q)) ** 2 for q in range(-Q, Q)]
    return sum(arr) / (2 * Q)


if __name__ == '__main__':
    N = 1000
    uniform_a = -2
    uniform_b = 2

    normal_mu = 0
    normal_sigma = 1

    system = System(1)
    Q = 100
    X = [random.uniform(uniform_a, uniform_b) for _ in range(N)]
    # Z = stats.cauchy.rvs(loc=0, scale=0.01, size=N)
    Z = [random.gauss(0, 0.5) for _ in range(N)]
    Y = [system.m(X[n]) + Z[n] for n in range(N)]
    T = [(X[n], Y[n]) for n in range(N)]
    h_space = arange(0.05, 2, 0.01)

    kernels = [K_boxcar, K_epanechnikov, K_cosine, K_gauss]
    for k in range(len(kernels)):
        valid_h_list = [valid_h(T, Q, h, system, kernels[k]) for h in h_space]
        min_h = h_space[valid_h_list.index(min(valid_h_list))]

        fig = pyplot.figure(k + 1)
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)

        pyplot.subplot(2, 1, 1)
        pyplot.title("valid(h)")
        pyplot.plot(h_space, valid_h_list)
        pyplot.ylabel("valid(h)")
        pyplot.xlabel("h")

        pyplot.subplot(2, 1, 2)
        pyplot.plot(X, m_N(T, X, min_h), 'r.', label='$m_{N}(x)$')
        pyplot.plot(X, [system.m(x) for x in X], 'g.', label='Charakterystyka systemu')
        pyplot.legend()

    pyplot.show()
