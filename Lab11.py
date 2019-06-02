import random

import numpy
from matplotlib import pyplot

a_s = 0.5
b_s = 10
teta_s = [b_s, a_s]
c = 0.1

N_max = 1000
U = [random.uniform(0, 1) for _ in range(N_max)]
# U = [1] + [0 for _ in range(1,N_max)]     #zad 2

V = [b_s * U[0]]
for n in range(1, N_max):
    V.append(b_s * U[n] + a_s * V[n - 1])

# ====================================================================
# sprawdzanie stabilnosci systemu
space = range(N_max)
pyplot.plot(space, Y)

# ============================= zad 4 ================================
# e_n = [random.uniform(-c, c) for _ in range(N_max)]
# Y = [V[n] + e_n[n] for n in range(N_max)]
# est_a = []
# est_b = []
# for N in range(50,1000,10):
#     Fi_N = [[U[1], Y[0]]]
#     for n in range(1, N):
#         Fi_N.append([U[n], Y[n - 1]])
#
#     Y_N = [0] + [a_s * U[n] + b_s * Y[n - 1] + e_n[n] + a_s * e_n[n - 1] for n in range(1, N)]
#
#     Fi_arr = numpy.array(Fi_N)
#     Y_N_arr = numpy.array(Y_N)
#     est_teta = ((Fi_arr.transpose().dot(Fi_arr))**(-1)).dot(Fi_arr.transpose()).dot(Y_N_arr)
#     est_a.append(0)
#     est_b.append(1)
#
# space_N = range(50,1000,10)
# a_N = [a_s for _ in space_N]
# b_N = [b_s for _ in space_N]
# pyplot.figure(1)
# pyplot.plot(space_N,a_N,'ro')
# pyplot.plot(space_N,est_a,'go')
# pyplot.figure(2)
# pyplot.plot(space_N,b_N,'r*')
# pyplot.plot(space_N,est_b,'g*')
# =======================================================================

# ============================= zad 4 ================================
L = 100


N_max = 500
for N in range(1,N_max+1):
    err_teta = []
    teta_l = []
    for l in range(L):
        e_n = [random.uniform(-c, c) for _ in range(N_max)]
        Y = [V[n] + e_n[n] for n in range(N_max)]
        Fi_N = [[U[1], Y[0]]]
        for n in range(1, N):
            Fi_N.append([U[n], Y[n - 1]])

        Y_N = [0] + [a_s * U[n] + b_s * Y[n - 1] + e_n[n] + a_s * e_n[n - 1] for n in range(1, N)]

        Fi_arr = numpy.array(Fi_N)
        Y_N_arr = numpy.array(Y_N)
        teta_l.append(((Fi_arr.transpose().dot(Fi_arr)) ** (-1)).dot(Fi_arr.transpose()).dot(Y_N_arr))
    sum([(numpy.array(teta) - numpy.array(teta_s)) for teta in teta_l]) #zad5?????


pyplot.show()
