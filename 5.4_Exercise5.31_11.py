from matplotlib.pylab import *
from numpy import *


def f(x, t):
    return exp(-(x-3*t)**2)*sin(3*pi(x-t))


t = 1
x = linspace(-4, 4, 1000)

plt.ion()
y = f(x, t)
lines = plt.plot(x, y)
plt.axis([x[-4], x[4], 1])
plt.xlabel('x')
plt.ylabel('y')

counter = 0
for t in t_values:
    y = f(x, t)
    lines[0].set_ydata(y)
    plt.legend(['t=%4.2f' % t])
    plt.draw()
    plt.savefig('tmp_%04d.png' % counter)
    counter += 1
plt.plot(x, y)
show()