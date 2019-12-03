import random
from math import atan, pi, sin

from matplotlib import pyplot
from Lab5_12 import K_boxcar


def m(U_n, c_2=1):
    return atan(c_2 * U_n)


def K(v):
    if abs(v) <= 0.5:
        return 1
    return 0


a_U = -1
b_U = 1
sigma_z = 0.2
N = 1000
L = 10
space_L = range(L + 1)
space_N = range(N+1)
U_N = [random.uniform(a_U, b_U) for _ in space_N]
V_N = [m(U_n) for U_n in U_N]
# pyplot.plot(U_N,V_N)
e_N = [random.gauss(0, sigma_z) for _ in space_N]
c1 = 0.5
lambda_L = [c1 ** l for l in space_L]
# c1 = [1 for l in range(L+1)]
Y_N = [sum([lambda_L[l] * V_N[n - l] for l in space_L]) + e_N[n] for n in space_N]

# ======================== zad 3 =====================================
# h_N = 0.5
# mi_N = []
# for u in U_N:
#     up = [Y_N[n] * K((U_N[n] - u) / h_N) for n in range(1, N)]
#     down = [K((U_N[n] - u) / h_N) for n in range(1, N)]
#     mi_N.append(sum(up) / sum(down))
# space_N = range(N)
# pyplot.figure(1)
# pyplot.plot(U_N, Y_N, "*")
# pyplot.figure(2)
# pyplot.plot(space_N, [m(u_n) for u_n in U_N], '*')
# pyplot.figure(3)
# pyplot.plot(U_N, mi_N, 'o')
# ====================================================================

# ======================== zad 4 =====================================

U_imp =[1] + [0 for _ in range(N)]
V_N_imp = [m(U_n) for U_n in U_N]
odp_imp = [sum([lambda_L[l]*V_N_imp[n-l] for l in space_L]) for n in space_N]
#
lambda_l = [sum([U_N[k-l]*Y_N[k] for k in range(l+1,N)])/(N-l) for l in space_L]
# space_N = range(N)

pyplot.plot(space_L, lambda_L,'g')
pyplot.plot(space_L, lambda_l,'r')

c= []
print("[c_l : val]")
for l in space_L:
    c.append(lambda_L[l]/lambda_l[l])
    print(l, " : ",c[l])
pyplot.show()
