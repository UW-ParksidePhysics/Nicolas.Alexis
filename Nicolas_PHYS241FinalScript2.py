from generate_matrix import generate_matrix
from lowest_eigenvectors import *
from numpy import linspace
import matplotlib.pyplot as plt

# 1. Generate the matrix according to the parameters
matrix = generate_matrix(minimum_x=float(-10), maximum_x=float(10), number_of_dimensions=100, potential_name='sinusoidal',
                    potential_parameter=float(200))
# 2. Use your lowest_eigenvectors function to calculate and return the three eigenvectors and eigenvalues of the matrix
eigenvalues, eigenvectors = lowest_eigenvectors(matrix)

# 3. Use NumPy's linspace to generate the grid of spatial points between -10 and 10 with Ndim points
n_dim = linspace(-10, 10, 100)

# 4. Plot the eigenvectors against the grid with a solid contrasting color curves
line1 = plt.plot(n_dim, eigenvectors[0][0:100])
line2 = plt.plot(n_dim, eigenvectors[1][0:100])
line3 = plt.plot(n_dim, eigenvectors[2][0:100])

display_graph = True
plt.axhline(y=0, color = 'black')
plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.ylim(-0.3, 0.3)
plt.text(-10, -0.27, 'Created by Alexis Nicolas 2020-05-12')
plt.title('Select Wavefunctions for a Sinusoidal Potential on a Spatial Grid of 100 Points')

plt.savefig("Nicolas.sinusoidal.Eigenvector0, 1, 2.png")
plt.show(display_graph)
