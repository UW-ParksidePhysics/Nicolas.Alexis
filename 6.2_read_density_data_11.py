# The goal of this exercise is to read the data and plot the density versus the temperature as distinct
# (small) circles for each data point. Let the program take the name of
# the data file as command-line argument. Apply the program to both
# # files.

import numpy as np
import matplotlib.pyplot as plt
import sys

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

def plot_data(x, y):
    plt.plot(x, y, 'o')
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.show()

plot_data(airdata['temperature'], airdata['density'])
plot_data(waterdata['temperature'], waterdata['density'])