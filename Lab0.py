import random
import time
from abc import abstractmethod
from typing import Any

from numpy import arange
from matplotlib import pyplot


class Generator(object):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def generate_random_numbers(self, seed, number):
        raise NotImplementedError


class SawtoothGenerator(Generator):

    def __init__(self, frequency=10) -> None:
        super().__init__()
        self._frequency = frequency
        self._sawtooth, self._values = self.sawtooth_wave(frequency)

    def sawtooth_wave(self, frequency=10) -> (dict, list):
        step = 0.01
        values = [x for x in arange(0, 1, step)]
        values = frequency * values
        t = [x for x in arange(0, 1, step / frequency)]

        sawtooth = {}
        iter = 0
        for val in values:
            sawtooth[t[iter]] = val
            iter += 1
        return sawtooth, values

    def show_sawtooth_wave(self, interpolate=True):
        if interpolate:
            pyplot.plot(self._sawtooth.keys(),
                        self._sawtooth.values(),
                        '*')
        else:
            pyplot.plot(self._sawtooth.keys(),
                        self._sawtooth.values())
        pyplot.show()

    def generate_random_numbers(self, seed: float, number: int) -> list:
        ret = []
        if seed < 0 or number < 0:
            return ret
        ret.append((seed * self._frequency) - int(seed * self._frequency))
        for i in range(1, number):
            ret.append(ret[i - 1] * self._frequency - int(ret[i - 1] * self._frequency))

        return ret

    @property
    def sawtooth(self):
        return self._sawtooth


class ModGenerator(Generator):

    def __init__(self, a=69069, c=1, mod=2 ** 32) -> None:
        super().__init__()
        self._mod = mod
        self._a = a
        self._c = c

    def generate_random_numbers(self, seed: float, number: int):
        ret = []
        if seed < 0 or number < 0:
            return ret

        ret.append(((self._a * seed) + self._c) % self._mod)

        for i in range(1, number):
            ret.append((self._a * ret[i - 1] + self._c) % self._mod)

        return ret


if __name__ == '__main__':
    fig = pyplot.figure(1)
    fig.text(0.5, 0.04, 'Wygenerowane liczby', ha='center', va='center')
    fig.text(0.06, 0.5, 'Liczba probek', ha='center', va='center', rotation='vertical')

    czestotliwosci = range(1,5)
    for val in czestotliwosci:
        sgen = SawtoothGenerator(val)
        pyplot.subplot(len(czestotliwosci),1,czestotliwosci.index(val)+1).set_title('Liczba zebow = '+str(val))
        liczby = sgen.generate_random_numbers(time.time(), 1000)
        pyplot.hist(liczby,20)

    fig2 = pyplot.figure(2)
    fig2.text(0.5, 0.04, 'Wygenerowane liczby', ha='center', va='center')
    fig2.text(0.06, 0.5, 'Liczba probek', ha='center', va='center', rotation='vertical')
    czestotliwosci = range(5,10)
    for val in czestotliwosci:
        sgen = SawtoothGenerator(val)
        pyplot.subplot(len(czestotliwosci),1,czestotliwosci.index(val)+1).set_title('Liczba zebow = '+str(val))
        liczby = sgen.generate_random_numbers(time.time(), 1000)
        pyplot.hist(liczby, 20)

    fig3 = pyplot.figure(3)
    fig3.text(0.5, 0.04, 'Wygenerowane liczby', ha='center', va='center')
    fig3.text(0.06, 0.5, 'Liczba probek', ha='center', va='center', rotation='vertical')
    czestotliwosci = [123,333,777,800]
    for val in czestotliwosci:
        sgen = SawtoothGenerator(val)
        pyplot.subplot(len(czestotliwosci),1,czestotliwosci.index(val)+1).set_title('Liczba zebow = '+str(val))
        liczby = sgen.generate_random_numbers(time.time(), 1000)
        pyplot.hist(liczby, 20)

    # params = [(), (40692, 0, 2 ** 31 - 249), ((2 ** 2) * (23 ** 7) + 1, 0, 2 ** 35), (1099087573, 0, 2 ** 32)]
    # names = ['Marsaglia (1972)', 'L\'Ecuyer (1988)', 'Zielinski (1966)', 'Fishman (1990)']
    # num = 1
    #
    #
    # fig = pyplot.figure(1)
    # fig.text(0.5, 0.04, 'Wygenerowane liczby', ha='center', va='center')
    # fig.text(0.06, 0.5, 'Liczba probek', ha='center', va='center', rotation='vertical')
    #
    # for param in params:
    #     mgen = ModGenerator()
    #
    #     numbers = mgen.generate_random_numbers(time.time(), 1000)
    #     pyplot.subplot(2, 2, num).set_title(names[num-1])
    #     pyplot.hist(numbers, 10)
    #     num += 1
sgen = SawtoothGenerator(777)