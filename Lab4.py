import random
import time

import Lab0
import Lab1
from matplotlib import pyplot
from numpy import arange


def empiric_distribution(values: list, space: list):
    returned_list = []
    for i in space:
        sum_of_values_lower_than_i = 0
        counter = 0
        for j in values:
            counter += 1
            if j <= i:
                sum_of_values_lower_than_i += 1
        returned_list.append( sum_of_values_lower_than_i / counter)
    return returned_list


generator = Lab1.Ex1()
D = []
N = range(100, 100000, 500)
# N = [1]
counter = 0
for nr_of_samples in N:
    keys = []
    for i in range(nr_of_samples):
        keys.append(random.uniform(0, 1))

    random_numbers = Lab1.Generator.generate_random_numbers(keys, generator)
    between = arange(0, 1, 0.01)

    empiric_dist = empiric_distribution(random_numbers, between)
    # pyplot.plot(empiric_dist.values(),empiric_dist.keys(), 'x')
    difference = []
    for key in range(len(empiric_dist)):
        difference.append(abs(empiric_dist[key] - generator.F(between[key])))
    D.append(max(difference))
    print(int(100*counter/len(N)), '%')
    counter+=1

keys = []
nr_of_samples = 10000
for i in range(nr_of_samples):
    keys.append(random.uniform(0, 1))

random_numbers = Lab1.Generator.generate_random_numbers(keys, generator)
between = arange(0, 1, 0.01)

values = Lab1.apply_for_all(between, generator.F)
pyplot.plot(between, values, 'o')

empiric_dist = empiric_distribution(values, between)
pyplot.figure(1)
pyplot.plot(empiric_dist, between, 'x')

pyplot.figure(2)
pyplot.plot(N, D, '*')
pyplot.show()
