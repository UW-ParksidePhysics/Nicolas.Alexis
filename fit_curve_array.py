from numpy import *
from quadratic_fit import coefficients, data

x = linspace(float(min(data[0])), float(max(data[0])))    # defining the x-range of the array
fit_curve = polyval(coefficients, x)    # generating the fit curve
array_data = column_stack((x, fit_curve))   # grouping the x, y coordinates


