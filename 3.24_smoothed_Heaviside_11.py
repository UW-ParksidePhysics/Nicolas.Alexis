from math import pi, sin


def H_eps(x, eps=0.01):
    if x < -eps:
        H_eps = 0
    elif -eps <= x <= eps:
        H_eps = 0.5 + (x / (2 * eps)) + ((1 / (2 * pi)) * sin((pi * x) / eps))
    elif x > eps:
        H_eps = 1
    return H_eps


def test_H_eps():
    print(H_eps(-1, eps=0.01))
    print(H_eps(-0.01, eps=0.01))
    print(H_eps(0, eps=0.01))
    print(H_eps(0.01, eps=0.01))
    print(H_eps(1, eps=0.01))
    return


test_H_eps()