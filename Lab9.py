import random
from math import sin, pi

import numpy
from matplotlib import pyplot

from Lab8 import scalarMultiplyArrays, estimate_a

if __name__ == '__main__':
    N_max = 400
    D = 20
    L = 30
    sigma = 1
    mu = [0 for _ in range(D)]

    b1 = 0.5
    sigma_epsilon = 1

    a_D = [sin(d * (pi / 4)) for d in range(1, D + 1)]
    a = numpy.array(a_D)
    ctr = 1
    for sigma_epsilon in [0.01,0.1,1,10]:
        pyplot.subplot(2,2,ctr)
        ctr +=1
        err_N = []
        for N in range(100, 2050, 50):
            X_N = [[random.gauss(mu[d], sigma) for d in range(D)] for _ in range(N)]
            d_space = range(D)
            n_space = range(N)
            # pyplot.plot(space, a_D, 'g')
            # pyplot.legend([r'$\hat{a}_{N}(N=50)$', r'$\hat{a}_{N}(N=500)$', 'a*'])

            # ================ zad 5 ============================
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
            a_l = []
            for l in range(1, L + 1):
                epsilon = [random.gauss(0, sigma_epsilon) for _ in range(N)]
                Z_N = [epsilon[0]] + [epsilon[n] + b1 * epsilon[n - 1] for n in range(1, N)]
                Y_N = [scalarMultiplyArrays(X_N[n], a_D) + Z_N[n] for n in range(N)]
                a_l.append(estimate_a(X_N[:N], Y_N[:N], N))

            err_N.append(sum([numpy.linalg.norm(a_N - a)**2 for a_N in a_l])/L)
        pyplot.plot(range(100, 2050, 50),err_N)
        pyplot.title(r'$\sigma_{\epsilon}^2='+str(sigma_epsilon)+'$')

# cov_a = ((X_matrix.transpose().dot(X_matrix)) ** (-1)).dot(X_matrix.transpose()).dot(R_mat).dot(X_matrix).dot(
#     (X_matrix.transpose().dot(X_matrix)) ** (-1))
# pyplot.subplot(2, 2, ctr)
# pyplot.imshow(cov_a)
# pyplot.colorbar()
# pyplot.title(r'$b_{1}=' + str(b1) + '$')
# ctr += 1
# ===================================================

    pyplot.show()
