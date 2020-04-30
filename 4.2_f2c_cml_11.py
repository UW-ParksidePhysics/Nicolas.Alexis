# convert f to c via command line
from numpy import *

F = input("Input Temperature in degrees F:")
Temperature = float(F)
C = (Temperature-32) * (5/9)
Converted_Temp = f'That is equivalent to {C:.2f} degrees C'
print(Converted_Temp)
