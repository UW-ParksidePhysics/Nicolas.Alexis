from math import pi
cd = 0.2 #drag coefficient
d = 1.2 #kg/m^3
a = .11 #meters
A = pi*a**2 #area m^2
m = .43 #kg
g = 9.81 #m/s^2
vh = 33.3
vs = 2.7
fdh = .5*cd*d*A*vh**2
fds = .5*cd*d*A*vs**2
print("Hard Kick", fdh)
print("Soft Kick", fds)
fg = m*g
Ratio = fdh/fg
print("Gravity Force", fg)
print("Ratio of drag force from hard kick to gravity force", Ratio)





