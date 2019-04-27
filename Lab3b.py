import random
import seaborn
import numpy
from matplotlib import pyplot

L=200
ran = range(10, 200, 10)
for i in ran:
    v = [(((random.gauss(i,L) - 0.5) * 2) / i) for k in range(i)]
print(v)

pyplot.hist(v,range=(-1,1))
pyplot.show()