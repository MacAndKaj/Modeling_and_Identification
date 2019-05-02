import random

from matplotlib import pyplot
from numpy.ma import arange

import Lab2
import Lab5_12


def empiric_error(f_n_list, real):
    arr = []
    for f_n in f_n_list:
        for m in range(len(f_n)):
            arr.append((f_n[m] - real[m]) ** 2)
    return sum(arr) / (len(f_n_list) * len(real))


if __name__ == '__main__':
    (a, b) = (0, 1)
    L = 10
    N = 500
    M = 100
    jump = abs(b - a) / M
    space = arange(a, b, jump)
    h_list = arange(0.01, 1, 0.01)
    print(len(space))
    normal = [Lab2.Ex1().f(x) for x in space]
    error = []
    for h in h_list:
        X_list = [[random.gauss(0, 1) for _ in range(N)] for _ in range(L)]  # LxN
        f_n_gauss_list = [[Lab5_12.kernel_estimator(X, x, h, Lab5_12.K_epanechnikov) for x in space] for X in X_list]
        error.append(empiric_error(f_n_gauss_list, normal))

    pyplot.plot(h_list, error,'*')
    pyplot.xlabel(r'$h_{N}$')
    pyplot.xlabel(r'$Err(\hat{f}_{N}(x))$')
    pyplot.show()
