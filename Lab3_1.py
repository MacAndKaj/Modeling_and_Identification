import numpy as np
from random import gauss
from matplotlib import pyplot

middleVal = 0
sizeOfNumberList = 1000


def get_s_quadr(generated_numbers: list):
    u = get_u(generated_numbers)
    arr = [(X_n - u) ** 2 for X_n in generated_numbers]
    return sum(arr) / len(generated_numbers)


def get_S_quadr(generated_numbers: list):
    u = get_u(generated_numbers)
    arr = [(X_n - u) ** 2 for X_n in generated_numbers]
    return sum(arr) / (len(generated_numbers) - 1)


def generate_numbers(size, middle, sigma):
    return [gauss(middle, sigma) for _ in range(size)]


def generate_numbers_cauchy(size):
    return np.random.standard_cauchy(size)


def get_u(numbers):
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    u_cauchy = []
    u = []
    s_quadr_cauchy = []
    s_quadr = []
    S_quadr_cauchy = []
    S_quadr = []

    N = 700
    space = range(10, N, 1)
    T_cauchy = generate_numbers_cauchy(N)
    T = generate_numbers(N, 0, 1)
    for n in space:
        u.append(get_u(T[0:n]))
        s_quadr.append(get_s_quadr(T[0:n]))
        S_quadr.append(get_S_quadr(T[0:n]))
        u_cauchy.append(get_u(T_cauchy[0:n]))
        s_quadr_cauchy.append(get_s_quadr(T_cauchy[0:n]))
        S_quadr_cauchy.append(get_S_quadr(T_cauchy[0:n]))

    fig = pyplot.figure(1)
    ax1 = fig.add_subplot(211)
    fig.add_subplot(212)
    ax1.title.set_text(r'$\hat{\mu}_{N}$')
    pyplot.subplot(2, 1, 1)
    pyplot.plot(space, u)
    pyplot.subplot(2, 1, 2)
    pyplot.plot(space, s_quadr,label=r'$\hat{s}^{2}_{N}$')
    pyplot.plot(space, S_quadr,label=r'$\hat{S}^{2}_{N}$')
    pyplot.legend()
    fig = pyplot.figure(2)
    ax1 = fig.add_subplot(211)
    fig.add_subplot(212)
    ax1.title.set_text(r'$\hat{\mu}_{N}$')
    pyplot.subplot(2, 1, 1)
    pyplot.plot(space, u_cauchy)
    pyplot.subplot(2, 1, 2)
    pyplot.plot(space, s_quadr_cauchy,label=r'$\hat{s}^{2}_{N}$')
    pyplot.plot(space, S_quadr_cauchy,label=r'$\hat{S}^{2}_{N}$')
    pyplot.legend()
    pyplot.show()
