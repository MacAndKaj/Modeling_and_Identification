import random
from math import pi, sqrt, cos
from matplotlib import pyplot
from numpy.ma import arange
from scipy import stats


class Model(object):

    def __init__(self, a=1) -> None:
        super().__init__()
        self._a = a

    def m(self, x):
        if 0 <= abs(x) < 1:
            return self._a * (x ** 2)
        if 1 <= abs(x) < 2:
            return 1
        else:
            return 0


class CosinusBase(object):

    def __init__(self, observations: dict, L=None) -> None:
        super().__init__()
        assert 'X' in observations and 'Y' in observations, "There must be X and Y observations"
        self._N = len(observations['Y'])
        self._T = observations
        self._L = L

    def m(self, x):
        return self.__g(x) / self.__f(x)

    def __L(self):
        if self._L is not None:
            return self._L
        return 100

    def __fi(self, k, x):
        assert k >= 0, "k is base function index, must be greater or equal to 0"
        if k == 0:
            return sqrt(1. / (2 * pi))
        else:
            return sqrt(1. / pi) * cos(k * x)

    def __g(self, x):
        return sum([self.__alfa(k) * self.__fi(k, x) for k in range(self.__L())])

    def __f(self, x):
        return sum([self.__beta(k) * self.__fi(k, x) for k in range(self.__L())])

    def __alfa(self, k):
        alfas = [self._T['Y'][n] * self.__fi(k, self._T['X'][n]) for n in range(self._N)]
        return sum(alfas) / self._N

    def __beta(self, k):
        betas = [self.__fi(k, self._T['X'][n]) for n in range(self._N)]
        return sum(betas) / self._N


# =============================  Generate signal =============================#
number_of_variables = 1000
model = Model()
ctr = 1
for sigm in [0.01, 0.1, 1, 10]:
    Z = stats.cauchy.rvs(loc=0, scale=sigm, size=number_of_variables)
    # Z = [random.gauss(0, 0.2) for _ in range(number_of_variables)]
    X = [random.uniform(-pi, pi) for _ in range(number_of_variables)]

    Y = []
    T_n = {'X': [], 'Y': []}
    for i in range(number_of_variables):
        Y.append(model.m(X[i]) + Z[i])
        T_n['X'].append(X[i])
        T_n['Y'].append(Y[i])

    space = arange(-pi, pi, 0.01)
    # ==================== ex 2 =========================
    # pyplot.figure(1)
    # pyplot.plot(X, Y, '*')
    # pyplot.plot(space, [model.m(x) for x in space], 'ro', linewidth=1)
    # pyplot.xlabel(r'$X_{n}$')
    # pyplot.ylabel(r'$Y_{n}$')
    # pyplot.legend(['Pomiary','Model'])
    # ====================================================

    # ==================== ex 3 =========================

    # pyplot.figure(2)
    # pyplot.plot(space, [model.m(x) for x in space], 'ro', linewidth=5)
    #
    # base = CosinusBase(T_n,10)
    # m_N = [base.m(x) for x in space]
    # pyplot.plot(space, m_N)
    # base = CosinusBase(T_n,20)
    # m_N = [base.m(x) for x in space]
    # pyplot.plot(space, m_N)
    # base = CosinusBase(T_n,50)
    # m_N = [base.m(x) for x in space]
    # pyplot.plot(space, m_N)
    # pyplot.legend([
    #     'model',
    #     'L=10',
    #     'L=20',
    #     'L=50',
    # ])
    # =====================================================

    # ==================== ex 4 ===========================
    pyplot.figure(4)
    pyplot.subplot(2, 2, ctr)
    pyplot.yscale('log')

    L_list = range(1, 101, 3)


    def valid_L(base_, model_):
        Q = 100
        errors = [(base_.m(2 * q / Q) - model_.m(2 * q / Q)) ** 2 for q in range(-Q, Q)]
        return sum(errors) / (2 * Q)


    error_L = []
    for l in L_list:
        base = CosinusBase(T_n, L=l)
        temp_error = valid_L(base, model)
        error_L.append(temp_error)

    best_L = L_list[error_L.index(min(error_L))]
    pyplot.plot(L_list, error_L)
    pyplot.title(r'$\gamma=' + str(sigm) + '$')
    pyplot.xlabel('L')
    pyplot.ylabel('err(L)')

    pyplot.figure(5)
    pyplot.subplot(2, 2, ctr)
    pyplot.plot(space, [model.m(x) for x in space], 'ro', linewidth=5)

    base = CosinusBase(T_n, best_L)
    m_N = [base.m(x) for x in space]
    pyplot.plot(space, m_N)
    pyplot.title(r'$\gamma='+str(sigm)+'$')
    ctr += 1
# =====================================================
pyplot.show()
