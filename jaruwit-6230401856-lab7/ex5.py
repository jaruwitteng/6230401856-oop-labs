import math


class Circle_constructed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def circle(num):
        area = math.pi * math.pow(num, 2)
        perimeter = 2 * math.pi * num
        return ("The circle with radius {}"" has the area as {:.2f}"
                "\n and the perimeter as {:.2f}".format(num, area, perimeter))


if __name__ == "__main__":
    print(Circle_constructed.circle(3))
    print(Circle_constructed.circle(4))
