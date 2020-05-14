"""Develop a Python script that:
takes reads in the data set given to you, fits the functional form given you, and produces a plot of the data points in
a scatter plot against the fit curve; and takes the matrix given to you and plots the lowest three eigenvectors against
a grid of points in space."""

from two_column_text_read import *
from univariate_statistics import *
from quadratic_fit import *
from equations_of_state import fit_eos
from convert_units import *
from fit_curve_array import *
from plot_data_with_fit import *
from annotate_graph import *
from lowest_eigenvectors import *
display_graph = True
# E. Read in the data into a NumPy array using your  two_column_text_read - function from the Final Review
file_name = "Au.Fm-3m.GGA-PBEsol.volumes_energies.dat"
data = two_column_text_read(file_name)

#   F. Get statistics on the data set using univariate_statistics function

statistics = univariate_statistics(data)

x_min = statistics[2]
x_max = statistics[3]
y_min = statistics[4]
y_max = statistics[5]

# 	G. Fit a quadratic polynomial to the data using quadratic_fit function

quadratic_coefficients = quadratic_fit(data)

# 	H. Pass 'vinet' to fit_eos

volumes = data[:, 0]
energies = data[:, 1]
vinet = fit_eos(volumes, energies, quadratic_coefficients, 'vinet')

# 	I. Write a convert_units module for atomic units
for i in range(len(data)):
    volume = data[i][0]
    energy = data[i][1]

    volume = convert_units(volume, 'Cubic Bohr/atom', 'Cubic Angstrom/atom')
    energy = convert_units(energy, 'Rydberg/atom', 'electron volts/atom')

    # data[i][0] = volume
    # data[i][1] = energy

for i in range(len(vinet)):
    bulk = vinet[i]
    bulk = convert_units(bulk, 'Rydberg/Cubic Bohr', 'Gigapascals')
    # vinet[i] = bulk

#   J. Plot data and fit function

Au_volume = linspace(x_min, x_max, len(vinet))
fit_curve = np.column_stack((Au_volume, vinet))

plot = plot_data_with_fit(data, fit_curve, 'bo', '-k')

plt.xlim(x_min - x_min*0.1, x_max + x_max*0.1)

plt.xlabel(r'$ \mathcal{eV/atom}\ $')
plt.ylabel(r'$ \mathit{Å^3/atom}\ $')
plt.title('Vinet Equation of State for Au in DFT GGA_PBEsol')
plt.text(100, -0.038, 'Created by Alexis Nicolas 2020-05-14')

#   K. Write a annotate_graph module


annotate_graph(chemical_symbol='Au', crystal_symmetry='GGA_PBEsol')
plt.savefig("Nicolas.Au.GGA_PBEsol.VinetEquationOfState.png")

plt.show(display_graph)




print("done")


def parse_file_name(file_name):
    parts = file_name.split(".")
    chemical_symbol = parts[0]
    crystal_symmetry_symbol = parts[1]
    density_function_approx = parts[2]

    return chemical_symbol, crystal_symmetry_symbol, density_function_approx
