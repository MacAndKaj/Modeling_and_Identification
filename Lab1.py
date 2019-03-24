import random
import time
from math import sqrt, log, e
from numpy import arange
from matplotlib import pyplot
from Lab0 import sgen
from abc import abstractmethod
start = -2
stop = 2

def apply_for_all(elements, func):
    ret = []
    for elem in elements:
        ret.append(func(elem))
    return ret


class Example:
    @abstractmethod
    def f(self, x):
        raise NotImplementedError

    @abstractmethod
    def F(self, x):
        raise NotImplementedError

    @abstractmethod
    def inv_F_x(self, y):
        raise NotImplementedError

    def dystrybuanta(self, s=0.01):
        between = arange(start,stop, s)
        values = apply_for_all(between, self.F)

        pyplot.subplot(5, 1, 2).set_title('Dystrybuanta')
        pyplot.plot(between, values, 'o')

    def rozklad(self, s=0.01):
        between = arange(start, stop, s)
        values = apply_for_all(between, self.f)

        pyplot.subplot(5, 1, 1).set_title('Rozklad')
        pyplot.plot(between, values, 'o')

    def histogram(self, s=0.01):
        keys = sgen.generate_random_numbers(time.time(), 1000)

        randoms = Generator.generate_random_numbers(keys,self)
        pyplot.subplot(5, 1, 3).set_title('Histogram')
        pyplot.hist(randoms,40)
        pyplot.subplot(5, 1, 4).set_title('Wartosci')
        pyplot.plot(randoms, range(len(keys)), '*')


class Ex1(Example):
    def f(self, x):
        if x < 0 or x > 1:
            return 0
        return 2 * x

    def F(self, x):
        if x > 1:
            return 1
        if x < 0:
            return 0
        return x ** 2

    def inv_F_x(self, y):
        return sqrt(y)


class Ex2(Example):
    def f(self, x):
        if -1 < x < 0:
            return x+1
        if 0 <= x < 1:
            return -x+1
        return 0

    def F(self, x):
        if x < -1:
            return 0
        if -1 < x < 0:
            return ((x**2)+(2*x)+1)/2
        if 0 <= x < 1:
            return 1-(((x**2)-(2*x)+1)/2)
        if 1 < x:
            return 1

    def inv_F_x(self, y):
        if 0 < y and y < 0.5:
            return sqrt(2*y)-1
        return 1-sqrt(-2 * (y-1))


class Ex3(Example):
    def f(self, x):
        if x < 0:
            return 0
        return e ** (-x)

    def F(self, x):
        if x < 0:
            return 0
        return 1-(e ** (-x))

    def inv_F_x(self, y):
        return -log(1-y)

# class Ex4(Example):
#     def f(self, x):
#         return (e**(-abs(x)))/2
#     def F(self, x):
#
#     def inv_F_x(self, y):


class Generator:

    @staticmethod
    def generate_random_numbers(randoms: list, Ex) -> list:
        ret = []
        for num in randoms:
            ret.append(Ex.inv_F_x(num))
        return ret


def all(Ex,numOfFigure):
    pyplot.figure(numOfFigure)
    Ex.rozklad(0.001)
    Ex.dystrybuanta(0.001)
    Ex.histogram()


if __name__=='__main__':
    all(Ex1(),1)
    all(Ex2(),2)
    all(Ex3(),3)
    pyplot.show()