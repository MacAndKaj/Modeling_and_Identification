import random
from matplotlib import pyplot
import Lab3_1


def get_Err_u_gauss(X, L, parameters):
    return sum([(Lab3_1.get_u(X) - parameters[0]) ** 2 for _ in range(L)]) / L


def get_Err_s(X, L, parameters):
    return sum([(Lab3_1.get_s_quadr(X) - parameters[1]) ** 2 for _ in range(L)]) / L


def get_Err_S(X, L, parameters):
    return sum([(Lab3_1.get_S_quadr(X) - parameters[1]) ** 2 for _ in range(L)]) / L


if __name__ == '__main__':
    L = [10,100]
    N = 1000
    N_range = range(10, N, 10)
    err_u = [[] for _ in L]
    err_s = [[] for _ in L]
    err_S = [[] for _ in L]
    fig = pyplot.figure(1)
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    ax1.title.set_text(r'$Err\{\hat{\mu}_{N},\mu\}$')
    ax2.title.set_text(r'$Err\{\hat{s}^{2}_{N},\sigma^{2}\}$')
    ax3.title.set_text(r'$Err\{\hat{S}^{2}_{N},\sigma^{2}\}$')

    for l in L:
        parameters=(0,1)
        X = [random.gauss(parameters[0], parameters[1]) for _ in range(N)]
        for N in N_range:
            err_u[L.index(l)].append(get_Err_u_gauss(X[0:N], l, parameters))
            err_s[L.index(l)].append(get_Err_s(X[0:N], l, parameters))
            err_S[L.index(l)].append(get_Err_S(X[0:N], l, parameters))

        pyplot.subplot(3, 1, 1)
        pyplot.plot(N_range, err_u[L.index(l)], label="L=" + str(l))
        pyplot.subplot(3, 1, 2)
        pyplot.plot(N_range, err_s[L.index(l)], label="L=" + str(l))
        pyplot.subplot(3, 1, 3)
        pyplot.plot(N_range, err_S[L.index(l)], label="L=" + str(l))
    pyplot.subplot(3, 1, 1)
    pyplot.legend()
    pyplot.subplot(3, 1, 2)
    pyplot.legend()
    pyplot.subplot(3, 1, 3)
    pyplot.legend()
    pyplot.show()
