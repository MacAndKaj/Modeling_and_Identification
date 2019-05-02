import math
from math import sqrt, exp, pi

import numpy
from matplotlib import pyplot
from numpy.ma import arange

from Lab1 import Example
from Lab3_1 import get_u
from Lab4 import empiric_distribution, D_N

file = open('ModelowanieLab4Data.txt', 'r')


class ExNormal(Example):
    def __init__(self, parameters) -> None:
        super().__init__()
        self._mu = parameters[0]
        self._sigma = parameters[1]

    def f(self, x):
        return exp(-((x - self._mu) ** 2) / (2 * self._sigma)) / sqrt(2 * self._sigma * pi)

    def F(self, x):
        return 0.5 * (1 + math.erf((x - self._mu) / sqrt(self._sigma)))


class ExCauchy(Example):
    def __init__(self, parameters) -> None:
        super().__init__()
        self._x0 = parameters[0]
        self._lambda = parameters[1]

    def f(self, x):
        return 1 / (pi * self._lambda * (1 + ((x - self._x0) / self._lambda) ** 2))

    def F(self, x):
        return 0.5 + (math.atan((x - self._x0) / self._lambda) / pi)


if __name__ == '__main__':
    numbers = []
    for i in file:
        numbers.append(float(i))
    file.close()

    space = arange(-3, 4, 0.01)
    F_N = empiric_distribution(numbers, space)
    pyplot.plot(space,numbers)
    pyplot.plot(space,F_N)
    pyplot.show()


    rozklady = [(1, 1), (0, 5)]
    for rozklad in rozklady:
        d = []
        N = range(10, 1000, 20)
        for n in N:
            F_empiric = empiric_distribution(numbers[0:n], space)
            d.append(D_N(F_empiric, space, ExNormal(rozklad)))
        pyplot.figure(rozklady.index(rozklad) + 1)
        pyplot.subplot(2, 1, 1)
        pyplot.plot(N, d, '*')
        pyplot.subplot(2, 1, 2)
        if rozklady.index(rozklad) == 0:
            pyplot.plot(space, [ExNormal((1, 1)).F(x) for x in space], '*', label='Normalny(1,1)')
        else:
            pyplot.plot(space, [ExNormal((0, 5)).F(x) for x in space], '*', label='Normalny(0,5)')
        pyplot.plot(space, F_N, label='$\hat{F}_{N}(x)$')
        pyplot.legend()

    d = []
    N = range(10, 1000, 20)
    for n in N:
        F_empiric = empiric_distribution(numbers[0:n], space)
        d.append(D_N(F_empiric, space, ExCauchy((0, 1))))
    pyplot.figure(3)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(N, d, '*')
    pyplot.subplot(2, 1, 2)
    pyplot.plot(space, [ExCauchy((0, 1)).F(x) for x in space], '*', label='Cauchy(0,1)')
    pyplot.plot(space, F_N, label='$\hat{F}_{N}(x)$')
    pyplot.legend()
    # sigma_quadr=[]
    # for i in range(1,len(space)):
    #     arr = [(x-[i])**2 for x in space[0:i]]
    #     sigma_quadr.append(sum(arr)/len(space[0:i]))
    #
    # pyplot.figure(5)
    # pyplot.plot(space[1:],sigma_quadr)
    pyplot.show()
