from matplotlib import pyplot

file = open('ModelowanieLab4Data.txt','r')

numbers = []
for i in file:
    numbers.append(float(i))
file.close()

