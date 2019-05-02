import random
import time

import Lab0
import Lab1
from matplotlib import pyplot
from numpy import arange

space = arange(-0.5, 1.5, 0.01)
N = 10000


def empiric_distribution(values: list, space):
    returned_list = []
    for x in space:
        sum_of_values_lower_than_i = 0
        counter = 0
        for X_n in values:
            counter += 1
            if X_n <= x:
                sum_of_values_lower_than_i += 1
        returned_list.append(sum_of_values_lower_than_i / counter)
    return returned_list


def empiric_variance(F_n, F, space):
    return [(F_n[i] - F(space[i])) ** 2 for i in range(len(space))]


def D_N(empiric_dist, space, ex=Lab1.Ex1()):
    d_n = []
    for i in range(len(empiric_dist)):
        d_n.append(abs(empiric_dist[i] - ex.F(space[i])))
    return max(d_n)


if __name__ == '__main__':
    # for nr_of_samples in [10,100,1000]:
    #     keys = [random.uniform(0, 1) for i in range(nr_of_samples)]
    #     randoms = Lab1.Generator.generate_random_numbers(keys, Lab1.Ex1())
    #
    #     F_empiric = empiric_distribution(randoms, space)
    #     empiric = pyplot.plot(space, F_empiric, 'o',label=r"$F_{N}(x)$ N="+str(nr_of_samples))
    #
    # F_real = [Lab1.Ex1().F(x) for x in space]
    # real = pyplot.plot(space, F_real, 'r',label=r"$F(x)$")
    # pyplot.legend()
    # pyplot.title("Wykres dystrybuanty empirycznej na tle prawdziwej")
    # pyplot.xlabel('x')
    # pyplot.ylabel('F(x)')
    # pyplot.grid()
    # D = []
    # n = range(10, N, 50)
    # keys = [random.uniform(0, 1) for i in range(N)]
    # randoms = Lab1.Generator.generate_random_numbers(keys, Lab1.Ex1())
    # F_real = [Lab1.Ex1().F(x) for x in space]
    # for nr_of_samples in n:
    #
    #     F_empiric = empiric_distribution(randoms[0:nr_of_samples], space)
    #
    #     D.append(D_N(F_empiric,space))
    #
    # pyplot.plot(n,D,'r*')
    #
    # pyplot.xlabel('N')
    # pyplot.ylabel('D(N)')
    # pyplot.plot(space, F_real, 'o')
    # pyplot.plot(space, F_empiric, '*')
    nr_of_samples = 500
    keys = [random.uniform(0, 1) for i in range(nr_of_samples)]
    randoms = Lab1.Generator.generate_random_numbers(keys, Lab1.Ex1())

    F_empiric = empiric_distribution(randoms, space)

    fig = pyplot.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.title.set_text(r'Dystrybuanta empiryczna')
    ax2.title.set_text(r'Estymator wariancji')

    pyplot.subplot(2, 1, 1)
    pyplot.plot(space, F_empiric)

    pyplot.subplot(2, 1, 2)
    pyplot.plot(space, empiric_variance(F_empiric, Lab1.Ex1().F, space))
    pyplot.show()
