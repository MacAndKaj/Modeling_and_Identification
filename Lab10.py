import random
import sys

import numpy
from matplotlib import pyplot

numpy.set_printoptions(threshold=sys.maxsize)
# N = 200
S = 10
space_s = range(S + 1)
b = [1] + [numpy.exp(-0.1 * s) for s in range(S)]
# for N in [50, 500, 1000]:

space_N_max = range(2001)
mu_U = 1
sigma_U = 0.1
white_noise = (0, 1)

# U_imp = [1] + [0 for _ in range(N - 1)]
U_N = [random.gauss(mu_U, sigma_U) for _ in space_N_max]
b_arr = numpy.array(b)
L = 100
alfa = 0.5
err_N = []
for N in range(100, 2050, 50):
    space_N = range(N)
    b_l = []
    for l in range(1, L + 1):

        e_n = [random.gauss(white_noise[0], white_noise[1]) for _ in space_N]
        Z_N = [e_n[0]] + [e_n[n] + alfa * e_n[n - 1] for n in range(1, N)]
        fi = [[U_N[0]] + [0 for _ in range(S)]]

        for n in range(1, N):
            fi.append([U_N[n]] + fi[n - 1][:S])
        fi_arr = numpy.array(fi)
        V_N = fi_arr.dot(b_arr)
        Z_N_arr = numpy.array(Z_N)
        Y_N_arr = V_N + Z_N_arr
        b_l.append((((fi_arr.transpose()).dot(fi_arr)) ** (-1)).dot((fi_arr.transpose())).dot(Y_N_arr))
    err_N.append(sum([(numpy.linalg.norm(b_l - b_arr)) ** 2 for b_N in b_l])/L)
err_N_2 = []
for N in range(100, 2050, 50):
    space_N = range(N)
    b_l = []
    for l in range(1, L + 1):

        e_n = [random.gauss(white_noise[0], white_noise[1]) for _ in space_N]
        Z_N = [e_n[0]] + [e_n[n] + alfa * e_n[n - 1] for n in range(1, N)]
        # b = [s**2 for s in range(S+1)]
        fi = [[U_N[0]] + [0 for _ in range(S)]]
        # fi_imp = [[U_imp[0]] + [0 for _ in range(S)]]

        for n in range(1, N):
            fi.append([U_N[n]] + fi[n - 1][:S])
            # fi_imp.append([U_imp[n]] + fi_imp[n - 1][:S])

        fi_arr = numpy.array(fi)
        # fi_imp_arr = numpy.array(fi_imp)

        V_N = fi_arr.dot(b_arr)
        # V_N_imp = fi_imp_arr.dot(b_arr)

        Z_N_arr = numpy.array(Z_N)
        Y_N_arr = V_N + Z_N_arr
        # Y_N_imp_arr = V_N_imp + Z_N_arr
        b_l.append((((fi_arr.transpose()).dot(fi_arr)) ** (-1)).dot((fi_arr.transpose())).dot(Y_N_arr))
    # b_N_imp_hat = numpy.linalg.inv(fi_imp_arr.transpose().dot(fi_imp_arr)).dot(fi_imp_arr.transpose()).dot(Y_N_imp_arr)
    err_N_2.append(sum([(numpy.linalg.norm(b_l - b_arr)) ** 2 for b_N in b_l])/L)

# legend.append(r'$\hat{b}_{N}$(N=' + str(N) + ')')
# pyplot.yscale('log')
pyplot.plot(range(100, 2050, 50), err_N)
pyplot.plot(range(100, 2050, 50), err_N_2)
pyplot.xlabel("N")
legend = [r'$Z_{N}=\{e_{n}\}$', r'$Z_{N}=e_{n}+\alpha e_{n-1}$']
pyplot.legend(legend)


#======================= zad 5 ===========================
# print(numpy.linalg.det(R_mat))
# pyplot.imshow(R_mat)
# pyplot.colorbar()
#========================================================


#======================= zad 6 ===========================
# err_N = []
# for N in range(100, 2050, 50):
#     R = []
#     for j in range(N):
#         R.append([])
#         for k in range(N):
#             if j == k:
#                 R[j].append(white_noise[1] + ((alfa ** 2) * white_noise[1]))
#             elif j == k - 1 or k == j - 1:
#                 R[j].append(alfa * white_noise[1])
#             else:
#                 R[j].append(0)
#     R_mat = numpy.array(R)
#     space_N = range(N)
#     b_l = []
#     R_inv = numpy.linalg.inv(R_mat)
#
#     for l in range(1, L + 1):
#
#         e_n = [random.gauss(white_noise[0], white_noise[1]) for _ in space_N]
#         Z_N = [e_n[0]] + [e_n[n] + alfa * e_n[n - 1] for n in range(1, N)]
#         fi = [[U_N[0]] + [0 for _ in range(S)]]
#         for n in range(1, N):
#             fi.append([U_N[n]] + fi[n - 1][:S])
#         fi_arr = numpy.array(fi)
#         V_N = fi_arr.dot(b_arr)
#         Z_N_arr = numpy.array(Z_N)
#         Y_N_arr = V_N + Z_N_arr
#         b_l.append(numpy.linalg.inv(fi_arr.transpose().dot(R_inv).dot(fi_arr)).dot(fi_arr.transpose().dot(R_inv).dot(Y_N_arr)))
#     err_N.append(sum([(numpy.linalg.norm(b_l - b_arr)) ** 2 for b_N in b_l])/L)
#     print(N)
#
# err_N_2 = []
# for N in range(100, 2050, 50):
#     space_N = range(N)
#     b_l = []
#     R = []
#     for j in range(N):
#         R.append([])
#         for k in range(N):
#             if j == k:
#                 R[j].append(white_noise[1] + ((alfa ** 2) * white_noise[1]))
#             elif j == k - 1 or k == j - 1:
#                 R[j].append(alfa * white_noise[1])
#             else:
#                 R[j].append(0)
#     R_mat = numpy.array(R)
#     R_inv = numpy.linalg.inv(R_mat)
#     for l in range(1, L + 1):
#         e_n = [random.gauss(white_noise[0], white_noise[1]) for _ in space_N]
#         Z_N = [e_n[0]] + [e_n[n] + alfa * e_n[n - 1] for n in range(1, N)]
#         fi = [[U_N[0]] + [0 for _ in range(S)]]
#         for n in range(1, N):
#             fi.append([U_N[n]] + fi[n - 1][:S])
#         fi_arr = numpy.array(fi)
#         V_N = fi_arr.dot(b_arr)
#         Z_N_arr = numpy.array(Z_N)
#         Y_N_arr = V_N + Z_N_arr
#
#         b_l.append(numpy.linalg.inv(fi_arr.transpose().dot(R_inv).dot(fi_arr)).dot(fi_arr.transpose().dot(R_inv).dot(Y_N_arr)))
#     err_N_2.append(sum([(numpy.linalg.norm(b_l - b_arr)) ** 2 for b_N in b_l])/L)
#     print(N)
#
# pyplot.plot(range(100, 2050, 50), err_N)
# pyplot.plot(range(100, 2050, 50), err_N_2)
# pyplot.xlabel("N")
# legend = [r'$Z_{N}=\{e_{n}\}$', r'$Z_{N}=e_{n}+\alpha e_{n-1}$']
# pyplot.legend(legend)
pyplot.show()
