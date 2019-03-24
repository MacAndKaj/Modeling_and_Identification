from time import time
from math import sqrt, log, e,pi
from numpy import arange
from matplotlib import pyplot
from Lab0 import sgen
import Lab1
from abc import abstractmethod

start = 0
stop = 0


class Example:
    @abstractmethod
    def f(self, x):
        raise NotImplementedError

    @abstractmethod
    def g(self, x):
        raise NotImplementedError

    def rozklad(self, s=0.01):
        between = arange(start, stop, s)
        values = Lab1.apply_for_all(between, self.f)

        # pyplot.subplot(4, 1, 2).set_title('Rozklad')
        pyplot.plot(between, values, 'o')


class Ex1(Example):

    def f(self, x):
        if -1 < x <= 0:
            return x + 1
        if 0 < x <= 1:
            return -x + 1
        return 0

    def g(self, x):
        return Lab1.Ex1().f(x)


ex1 = Ex1()


class Ex2(Example):

    def f(self, x):
        if 0 < x <= 0.01:
            return 50
        return 0

    def g(self, x):
        return Lab1.Ex1().f(x)


ex2 = Ex2()


class Ex3(Example):

    def f(self, x):
        return 2*pi/x

    def g(self, x):
        return Lab1.Ex1().f(x)


ex3 = Ex3()


def elimination_method(Ex, c):
    while True:
        u = sgen.generate_random_numbers(time(), 1)[0]
        x = Lab1.Ex1().inv_F_x(sgen.generate_random_numbers(time(), 1)[0])
        val_g = Ex.g(x)
        val_f = Ex.f(x)
        if c * u * val_g <= val_f:
            return x


def generate_random_numbers(Ex, c, numbers: int):
    ret = []
    for i in range(numbers):
        ret.append(elimination_method(Ex, c))
    return ret


randoms = generate_random_numbers(ex3, 1.01, 1000)
pyplot.figure(1)
ex1.rozklad()
pyplot.figure(2)
pyplot.hist(randoms)
pyplot.show()
