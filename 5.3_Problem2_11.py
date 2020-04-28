from matplotlib.pylab import *
from numpy import *

sd1 = float(.5)
sd2 = float(1)
sd3 = float(1.5)
mu = 5
x = linspace(0,10,100)
y1 = (1/(sqrt(2*pi)*sd1))*exp(-(x-mu)**2/(2*sd1**2))
y2 = (1/(sqrt(2*pi)*sd2))*exp(-(x-mu)**2/(2*sd2**2))
y3 = (1/(sqrt(2*pi)*sd3))*exp(-(x-mu)**2/(2*sd3**2))
plot(x, y1, '--', label='.5 sigma')
plot(x, y2, '-', label='1 sigma')
plot(x, y3, ':', label='1.5 sigma')
xlim(0, 10)
ylim(0, 1)
xlabel('x')
ylabel('(x-5),sigma')
show()
