import matplotlib.pyplot as plt
import numpy as np

#create two lists
x = []
y = []

#create file object for reading
infile = open('xy.dat.txt', 'r')

#read file line by line
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

#concatenate values
x, y = np.array(x), np.array(y)

print('Minimum x value = %f' % x.min())
print ('Maximum x value = %f' % x.max())
print ('Minimum y value = %f' % y.min())
print ('Maximum y value = %f' % y.max())

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


