from numpy import polyfit


def quadratic_fit(data):
    quadratic_coefficients = polyfit(data[:,0], data[:,1], 2)  # create a second order quadratic equation, variables from two_column_text_read

    return quadratic_coefficients

