import matplotlib.pyplot as plt

from matplotlib.animation import animation

import numpy as np

m = 0
s_min = 0.2
s_max = 2
x = np.linspace(m - 3 * s_max, m + 3 * s_max, 1000)
s_values = np.linspace(s_max, s_min, 30)
# f is max for x=m; smaller s gives larger max value
max_f = f(m, m, s_min)


def f(x, m, s):
    return (1.0 / (np.sqrt(2 * np.pi) * s)) * np.exp(-0.5 * ((x - m) / s) ** 2)


anim = animation.FuncAnimation(fig, frame, all_args, interval=150, init_func=init, blit=True)
fig = plt.figure()
plt.axis([x[0], x[-1], -0.1, max_f])
lines = plt.plot([], [])
plt.xlabel('x')
plt.ylabel('f')


def init():
    lines[0].set_data([], [])  # empty plot
    return lines


def frame(args):
    frame_no, s, x, lines = args
    y = f(x, m, s)
    lines[0].set_data(x, y)
    return lines


anim = animation.FuncAnimation(fig, frame, all_args, interval=150, init_func=init, blit=True)

anim.save('movie1.mp4', fps=5)   # movie in MP4 format