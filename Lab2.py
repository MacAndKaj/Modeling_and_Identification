import random
from time import time
from math import sqrt, log, e, pi
from numpy import arange
from matplotlib import pyplot

import Lab0
from Lab0 import sgen
import Lab1
from abc import abstractmethod

nr_of_samples = 10000
start = 0
stop = 0


class Example:
    @abstractmethod
    def f(self, x):
        raise NotImplementedError

    @abstractmethod
    def g(self, x):
        raise NotImplementedError

    @abstractmethod
    def generate_X(self):
        raise NotImplementedError


class Ex1(Example):

    def __init__(self) -> None:
        super().__init__()
        self._a = -1
        self._b = 1

    def f(self, x):
        if -1 < x <= 0:
            return x + 1
        if 0 < x <= 1:
            return -x + 1
        return 0

    def g(self, x):
        if self._a < x < self._b:
            return 1 / (self._b - self._a)
        return 0

    def generate_X(self):
        return random.uniform(self._a, self._b)


ex1 = Ex1()


class Ex2(Example):

    def __init__(self) -> None:
        super().__init__()
        self._a = 0
        self._b = 1

    def f(self, x):
        if 0 < x <= 0.01:
            return 50
        if 0.01 < x <= 1:
            return 1
        return 0

    def g(self, x):
        if self._a < x < self._b:
            return 1 / (self._b - self._a)
        return 0

    def generate_X(self):
        return random.uniform(self._a, self._b)


ex2 = Ex2()


class Ex3(Example):

    def __init__(self, r) -> None:
        super().__init__()
        self._r = r
        self._uniformGen = Lab0.SawtoothGenerator(-r, r, 119)

    def f(self, x):
        if -self._r <= x <= self._r:
            return sqrt(self._r ** 2 - x ** 2)
        return 0

    def g(self, x):
        if -self._r < x < self._r:
            return 1 / (2 * self._r)
        return 0

    def generate_X(self):
        return random.uniform(-self._r,self._r)


ex3 = Ex3(1)


class Ex4(Example):

    def f(self, x):
        return (1 / sqrt(2 * pi)) * e ** (-(x ** 2) / 2)

    def g(self, x):
        return Lab1.Ex4(1, 0).f(x)

    def generate_X(self):
        return Lab1.Generator.generate_random_numbers(sgen.generate_random_numbers(time(), 1), Lab1.Ex4(1, 0))[0]


ex4 = Ex4()


def elimination_method(Ex, c):
    while True:
        u = random.uniform(0,1)
        x = Ex.generate_X()
        if c * Ex.g(x) * u <= Ex.f(x):
            return x


def generate_random_numbers(Ex, c, numbers: int):
    ret = []
    for i in range(numbers):
        ret.append(elimination_method(Ex, c))
    return ret


def ex1_check():
    c_param = 2
    between = arange(-2, 2, 0.0001)
    values1 = Lab1.apply_for_all(between, ex1.f)
    values2 = Lab1.apply_for_all(between, ex1.g, c_param)
    randoms = generate_random_numbers(ex1, c_param, nr_of_samples)

    pyplot.figure(1)
    pyplot.subplot(2, 1, 1).set_title('Gęstość rozkladu')
    pyplot.plot(between, values2, 'o', label='cg(x)')
    pyplot.plot(between, values1, '*', label='f(x)')
    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                  ncol=2, mode="expand", borderaxespad=0.)

    pyplot.subplot(2, 1, 2).set_title('Histogram wygenerowanych liczb')
    pyplot.hist(randoms, 40)
    pyplot.show()


def ex2_check():
    c_param = 50
    between = arange(-2, 2, 0.0001)
    values1 = Lab1.apply_for_all(between, ex2.f)
    values2 = Lab1.apply_for_all(between, ex2.g, c_param)
    randoms = generate_random_numbers(ex2, 50, nr_of_samples)

    pyplot.figure(2)
    pyplot.subplot(2, 1, 1).set_title('Gęstość rozkladu')
    pyplot.plot(between, values2, 'o', label='cg(x)')
    pyplot.plot(between, values1, '*', label='f(x)')

    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                  ncol=2, mode="expand", borderaxespad=0.)
    pyplot.subplot(2, 1, 2).set_title('Histogram wygenerowanych liczb')
    pyplot.hist(randoms, 40)
    pyplot.show()


def ex3_check():
    c_param = 2
    between = arange(-2, 2, 0.0001)
    values1 = Lab1.apply_for_all(between, ex3.f)
    values2 = Lab1.apply_for_all(between, ex3.g, c_param)
    randoms = generate_random_numbers(ex3, c_param, nr_of_samples)

    pyplot.figure(3)
    pyplot.subplot(2, 1, 1).set_title('Gęstość rozkladu')
    pyplot.plot(between, values2, 'o', label='cg(x)')
    pyplot.plot(between, values1, '*', label='f(x)')
    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                  ncol=2, mode="expand", borderaxespad=0.)


    pyplot.subplot(2, 1, 2).set_title('Histogram wygenerowanych liczb')
    pyplot.hist(randoms, 40)
    pyplot.show()


def ex4_check():
    c_param = sqrt(2 * e / pi)
    randoms = generate_random_numbers(ex4, c_param, nr_of_samples)
    print(randoms)
    pyplot.figure(4)
    between = arange(-5, 5, 0.0001)
    values1 = Lab1.apply_for_all(between, ex4.f)
    values2 = Lab1.apply_for_all(between, ex4.g, c_param)

    pyplot.subplot(2, 1, 1).set_title('Gęstość rozkladu')
    pyplot.plot(between, values2, 'o', label='cg(x)')
    pyplot.plot(between, values1, '*', label='f(x)')
    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                  ncol=2, mode="expand", borderaxespad=0.)

    pyplot.subplot(2, 1, 2).set_title('Histogram wygenerowanych liczb')
    pyplot.hist(randoms, 50)
    pyplot.show()


if __name__ == '__main__':
    ex1_check()
    ex2_check()
    ex3_check()
    ex4_check()
