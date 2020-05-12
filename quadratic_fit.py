from numpy import polyfit
from two_column_text_read import data
coefficients = polyfit(data[0], data[1], 2)  # create a second order quadratic equation, variables from two_column_text_read
print(coefficients)
