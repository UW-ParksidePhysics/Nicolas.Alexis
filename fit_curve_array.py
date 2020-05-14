import numpy as np
def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points = 100):
    x = np.linspace(float(minimum_x), float(maximum_x), number_of_points)    # defining the x-range of the array
    fit_curve = np.polyval(quadratic_coefficients, x)    # generating the fit curve
    array_data = np.column_stack((x, fit_curve))   # grouping the x, y coordinates
    return array_data

