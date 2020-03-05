from math import pi
from math import log
M = 47 #g
p = 1.038 #g/cm^3
c = 3.7 #j/gK
K = 5.4e-3
Tw = 100 #C
Ty = 70 #C
To1 = 4 #C
To2 = 20 #C

ft = (M**(2/3)*c*p**(1/3))/((K*pi**2)*((4*pi/3)**2/3))
st1 = (.76*((To1-Tw)/(Ty-Tw)))
st2 = (.76*((To2-Tw)/(Ty-Tw)))
t1 = ft*log(st1)
t2 = ft*log(st2)
print("From fridge the egg would take", t1, "seconds")
print("At room temperature the egg would take", t2, "seconds")
