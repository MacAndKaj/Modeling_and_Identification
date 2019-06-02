import random
from math import sin, pi

import numpy
from matplotlib import pyplot,rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# N = 100
D = 10
L = 20
mu = 0
sigma = 1


def scalarMultiplyArrays(a: list, b: list):
    assert len(a) == len(b), "Must be in same size"
    arr = [a[i] * b[i] for i in range(len(a))]
    return sum(arr)


def estimate_a(X_N, Y_N, n=100):
    X_matrix = numpy.matrix(X_N[:n])
    Y_Vector = numpy.array(Y_N)
    XtX_inv = (X_matrix.transpose() * X_matrix) ** (-1)
    XtX_invXt = XtX_inv * (X_matrix.transpose())
    return XtX_invXt.dot(Y_Vector)


if __name__ == '__main__':
    a_D = [sin(d * (pi / 4)) for d in range(1, D + 1)]
    X_N = [[random.gauss(mu, sigma) for _ in range(D)] for _ in range(1000)]

    # ================ zad 3 ============================
    # sigma_z = 1
    # N_max = [50,500]
    # pyplot.figure(1)
    # space = range(D)
    # for N in N_max:
    #     Z_n = [random.gauss(mu, sigma_z) for _ in range(N)]
    #     Y_N = [scalarMultiplyArrays(X_N[:N+1][n], a_D) + Z_n[n] for n in range(N)]
    #
    #
    #
    #
    #     estimator_a = estimate_a(X_N, Y_N,N)
    #     est_a_list = list(numpy.array(estimator_a).reshape(-1, ))
    # # numpy.eye(D, D, sigma_z)
    #     pyplot.plot(space, est_a_list, 'o')
    # pyplot.plot(space, a_D, 'g')
    # pyplot.legend([r'$\hat{a}_{N}(N=50)$',r'$\hat{a}_{N}(N=500)$','a*'])

    # ================ zad 4 ============================
    N = 1000
    sigma_z = 1
    space = range(D)
    Z_n = [random.gauss(mu, sigma_z) for _ in range(N)]
    Y_N = [scalarMultiplyArrays(X_N[:N + 1][n], a_D) + Z_n[n] for n in range(N)]

    # ================ zad 3 ============================
    pyplot.figure(2)
    pyplot.subplots(2,2)
    cnt = 1
    for N_max in [50,100,500,1000]:
        estimator_a = estimate_a(X_N[:N_max], Y_N[:N_max], N_max)
        est_a_list = list(numpy.array(estimator_a).reshape(-1, ))
        # numpy.eye(D, D, sigma_z)
        # pyplot.plot(space, est_a_list, 'o')
        X_matrix = numpy.matrix(X_N[:N_max])
        XtX_inv = (X_matrix.transpose() * X_matrix) ** (-1)
        cov_a = sigma_z * XtX_inv

        pyplot.subplot(2,2,cnt)
        cnt+=1
        pyplot.imshow(cov_a)
        pyplot.colorbar()
        pyplot.title(r'$N=$'+str(N_max))
    # ===================================================

    # err_N = []
    # Z_n_l = [[random.gauss(mu, sigma_z) for _ in range(N)] for _ in range(L)]
    # for n_N in range(N+1):
    #     err_l = []
    #     for l in range(L):
    #         Y_N = [scalarMultiplyArrays(X_N[n], a_D) + Z_n_l[l][n] for n in range(1,n_N+1)]
    #         estimator_a = estimate_a(X_N, Y_N)
    #         err_l.append(numpy.linalg.norm(estimator_a-numpy.array(a_D))**2)
    #     err_N.append(sum(err_l)/L)
    #
    # space_N = range(1, N)
    # a_D_array = numpy.array(a_D)
    # pyplot.figure(3)
    #
    # pyplot.yscale('log')
    # for sigma_z in [0.01, 0.1, 1, 10]:
    #     print(sigma_z)
    #     err_a_N = []
    #     for n_end in space_N:
    #         est_N_l = []
    #         for l in range(L):
    #             Z_n = [random.gauss(mu, sigma_z) for _ in range(n_end)]
    #             Y_N = [scalarMultiplyArrays(X_N[n], a_D) + Z_n[n] for n in range(n_end)]
    #             estimator_a = estimate_a(X_N[:n_end], Y_N)
    #             est_N_l.append(list(numpy.array(estimator_a).reshape(-1, )))
    #
    #         err = []
    #         for est_N in est_N_l:
    #             est_N_array = numpy.array(est_N)
    #             diff = (est_N_array - a_D_array).tolist()
    #             err.append(sum([a ** 2 for a in diff]))
    #         err_a_N.append(sum(err) / L)
    #
    #     pyplot.plot(space_N, err_a_N)
    # pyplot.legend([r'$\sigma^{2}_{Z}=0.01$', r'$\sigma^{2}_{Z}=0.1$', r'$\sigma^{2}_{Z}=1$', r'$\sigma^{2}_{Z}=10$'])
    # pyplot.ylabel(r'$Err\{\hat{a}_N\}$')
    # pyplot.xlabel('N')


    pyplot.show()
