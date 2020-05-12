import matplotlib.pyplot as plt
from fit_curve_array import x, fit_curve

plt.plot(x, fit_curve)  # plotting the array data
plt.xlabel("Volume")
plt.ylabel("Energy")
plt.show()