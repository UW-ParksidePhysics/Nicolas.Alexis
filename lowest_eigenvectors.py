from numpy import linalg

def lowest_eigenvectors(square_matrix, number_of_eigenvectors = 3):
    (V, D) = linalg.eig(square_matrix)
    eigenvalues = V[slice(number_of_eigenvectors)]
    eigenvectors = D[slice(number_of_eigenvectors)]
    return eigenvalues, eigenvectors
