import numpy as np
import matplotlib.pyplot as plt


dt = float(input("Enter a value for dt: "))
def velocity(a, dt):
    n = len(a)
    v = np.zeros(n)
    for k in range(1, n):
        v[k] = v[k-1] + (a[k-1] + a[k])/2
    v *= dt
    return v


acc = np.loadtxt('acc.txt')
vel = velocity(acc, dt)
time = np.array([i * dt for i in range(0, len(acc))])

plt.plot(time, acc)
plt.plot(time, vel)
plt.xlabel('Time')
plt.legend(['Acceleration', 'Velocity'])
plt.title('Time dependence of object acceleration and velocity')
plt.show()