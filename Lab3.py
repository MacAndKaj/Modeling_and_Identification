from math import sqrt
from random import gauss
from matplotlib import pyplot

middleVal = 0
sigmaVal = 0.2
sizeOfNumberList = 1000


def get_s(generated_numbers: list):
    ret_sum = 0
    for num in generated_numbers:
        ret_sum = ret_sum + (num - middleVal) ** 2
    return sqrt(ret_sum / len(generated_numbers))


def generate_numbers(size, middle, sigma):
    numbers = []
    for i in range(size):
        numbers.append(gauss(middle, sigma))

    return numbers


def get_u(numbers):
    return sum(numbers) / len(numbers)


def get_Err_u(generated_numbers, middle, L):
    err = []
    for l in range(L):
        err.append((get_u(generated_numbers) - middle) ** 2)

    return sum(err) / len(err)

def get_Err_s(generated_numbers, sigma, L):
    err = []
    for l in range(L):
        err.append((get_s(generated_numbers) - sigma) ** 2)

    return sum(err) / len(err)


ran = range(1, sizeOfNumberList)
err_u = []
err_s = []
for i in range(1, sizeOfNumberList):
    (numbers) = generate_numbers(i, middleVal, sigmaVal)
    L = 10
    err_u.append(get_Err_u(numbers, middleVal, L))
    err_s.append(get_Err_s(numbers,sigmaVal,L))






pyplot.figure(1)
pyplot.plot(ran, err_u,'*')
pyplot.figure(2)
pyplot.plot(ran, err_s,'*')



pyplot.show()

