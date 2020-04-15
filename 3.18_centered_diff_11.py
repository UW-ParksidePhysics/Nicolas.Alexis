### Part a ###
def diff(f, x, h):
    derive = ((f(x + h) - f(x - h)) / (2 * h))
    return derive


### Part c ###
def application(f, x, h, exact_derivative):
    derive = diff(f, x, h)
    error = exact_derivative - derive
    print()
    print("Approximate Derivative =", derive)
    print("Exact Derivative =", exact_derivative)
    print(derive, "-", exact_derivative, "=", error)
    return


from math import exp, cos, pi, log


def f(x):
    f = exp(x)
    return f


def g(x):
    g = exp(-2 * (x ** 2))
    return g


def h(x):
    h = cos(x)
    return h


def i(x):
    i = log(x)
    return i


application(f, 0, 0.01, 1)
application(g, 0, 0.01, 0)
application(h, (2 * pi), 0.01, 0)
application(i, 1, 0.01, 1)