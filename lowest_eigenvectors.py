from numpy import loadtxt, linalg, asarray

data = loadtxt(input('Input Matrix File: '))  # import the data
array = asarray(data)  # convert data to array
(w, v) = linalg.eig(array)  # find eigenvalues/eigenvectors
w.sort()  # change eigenvalues to ascending order
print(w) #print eigenvalues
# print(v) #print eigenvectors

#Help from Erik H.