import numpy as np
import matplotlib.pyplot as plt
import os

#similar code to 6.2
# get data from density and water txt files

##trying again

airfile = open('density_airt.txt', 'r')
airdata = {'temperature': [], 'density': []}

waterfile = open('density_water.txt', 'r')
waterdata = {'temperature': [], 'density': []}


for line in airfile:
    if line.isspace() or line.lstrip()[0] == '#':
        continue
    else:
        values = line.split()
        airdata['temperature'].append(float(values[0]))
        airdata['density'].append(float(values[1]))
airdata['temperature'] = np.array(airdata['temperature'])
airdata['density'] = np.array(airdata['density'])
airfile.close()

for line in waterfile:
    if line.isspace() or line.lstrip()[0] == '#':
        continue
    else:
        values = line.split()
        waterdata['temperature'].append(float(values[0]))
        waterdata['density'].append(float(values[1]))
waterdata['temperature'] = np.array(waterdata['temperature'])
waterdata['density'] = np.array(waterdata['density'])
waterfile.close()


def fit_data(x, y, substance):
    plt.plot('x', 'y', 'o')

    for deg, linecol in [(1,'r'), (2,'b')]:
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--')

        plt.xlabel('Temperature')
        plt.ylabel('Density')
        plt.title('Temperature dependence of density')
        plt.legend(['data', 'fitted degree 1 polynomial', 'fitted degree 2 polynomial'])
        plt.show()



fit_data(airdata['temperature'], airdata['density'], 'air')
fit_data(waterdata['temperature'], waterdata['density'], 'water')
