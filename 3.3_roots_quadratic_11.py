from math import sqrt
a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))
D2 = b ** 2 - 4 * a * c
if a == 0:
    print('a Cannot Equal Zero')

if D2 >= 0:
    D = sqrt(D2)
    x1 = (-b - D) / (2 * a)
    x2 = (2 * c) / (-b - D)
    R = [x1, x2]
    print("test_roots_float")
    print(R)