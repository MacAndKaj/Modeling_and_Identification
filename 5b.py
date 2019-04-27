import random

import numpy
from matplotlib import pyplot

from Lab1 import Ex1, Generator

nr_of_samples=500
keys = []
for i in range(nr_of_samples):
    keys.append(random.uniform(0, 1))


def K_boxcar(x):
    if abs(x) <= 1:
        return 0.5
    else:
        return 0


randoms = Generator.generate_random_numbers(keys, Ex1())
pyplot.subplot(5, 1, 4).set_title('Histogram')
pyplot.hist(randoms, 50)
pyplot.subplot(5, 1, 5).set_title('Wartosci')
pyplot.plot(randoms, range(len(keys)), '*')

estymator = []
random_numbers = []

for _ in range(k):
    random_numbers.append(random.gauss(1, 1))


h_list = numpy.arange(1, 0.01, -0.25)
f_n_list = []
gauss_list = []

przedzial = numpy.arange(-2, 3, 0.001)
for h in h_list:
    estymator = []
    for x in przedzial:
        suma = 0
        for val in random_numbers:
            suma += K_boxcar((val - x) / h)
        estymator.append(suma / (k * h))

    f_n_list.append(estymator)

for x in przedzial:
    gauss_list.append(Ex1().f(x))

labels = []
i = 0
pyplot.figure(1)
for f in f_n_list:
    pyplot.plot(przedzial, f)
    labels.append('h=' + str(h_list[i]))
    i += 1
pyplot.legend(labels)
pyplot.plot(przedzial, gauss_list)
