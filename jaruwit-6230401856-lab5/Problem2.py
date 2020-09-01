import math


def hypotenuse(a, b):
    print("sqrt({}^2 + {}^2 = {})".format(a, b, math.sqrt(math.pow(a, 2) + math.pow(b, 2))))


hypotenuse(3.0, 4.0)
hypotenuse(3, 4)
hypotenuse(3, 4.0)
