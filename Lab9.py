import random
from math import sin, pi

import numpy
from matplotlib import pyplot

from Lab8 import scalarMultiplyArrays, estimate_a

if __name__ == '__main__':
    N_max = 400
    D = 20
    # L = 20
    sigma = 1
    mu = [0 for _ in range(D)]

    b1 = 0.5
    sigma_epsilon = 1

    a_D = [sin(d * (pi / 4)) for d in range(1, D + 1)]
    X_N = [[random.gauss(mu[d], sigma) for d in range(D)] for _ in range(N_max)]

    epsilon = [random.gauss(0, sigma_epsilon) for _ in range(N_max)]
    Z_N = [epsilon[0]] + [epsilon[n] + b1 * epsilon[n - 1] for n in range(1, N_max)]
    Y_N = [scalarMultiplyArrays(X_N[n], a_D) + Z_N[n] for n in range(N_max)]

    d_space = range(D)
    n_space = range(N_max)
    # estimator_a = estimate_a(X_N, Y_N)
    # est_a_list = list(numpy.array(estimator_a).reshape(-1, ))
    # numpy.eye(D, D, sigma_z)
    pyplot.figure(1)
    space = range(D)

    for N in [50, 500]:
        estimator_a = estimate_a(X_N[:N], Y_N[:N], N)
        est_a_list = list(numpy.array(estimator_a).reshape(-1, ))
        pyplot.plot(space, est_a_list, 'o')
    pyplot.plot(space, a_D, 'g')
    pyplot.legend([r'$\hat{a}_{N}(N=50)$', r'$\hat{a}_{N}(N=500)$', 'a*'])

    # ================ zad 5 ============================
    pyplot.figure(2)
    estimator_a = estimate_a(X_N, Y_N, N_max)
    est_a_list = list(numpy.array(estimator_a).reshape(-1, ))
    pyplot.plot(space, est_a_list, 'o')
    Z_matrix = numpy.array(Z_N)
    X_matrix = numpy.array(X_N)
    R = []
    for j in n_space:
        R.append([])
        for k in n_space:
            if j == k:
                R[j].append(sigma_epsilon + ((b1 ** 2) * sigma_epsilon))
            elif j == k - 1 or k == j - 1:
                R[j].append(b1 * sigma_epsilon)
            else:
                R[j].append(0)
    R_mat = numpy.array(R)
    pyplot.figure(2)
    pyplot.imshow(R_mat)
    pyplot.colorbar()

    pyplot.figure(3)
    cov_a = ((X_matrix.transpose().dot(X_matrix)) ** (-1)).dot(X_matrix.transpose()).dot(R_mat).dot(X_matrix).dot(
        (X_matrix.transpose().dot(X_matrix)) ** (-1))
    pyplot.imshow(cov_a)
    pyplot.colorbar()
    pyplot.title('Macierz kowariancji')
    # ===================================================

    pyplot.show()
