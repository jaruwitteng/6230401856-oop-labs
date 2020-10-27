
import abc
import random


class Shape(abc.ABC):
    @abc.abstractmethod
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def draw(self):
        print("Drawing a rectangles with width {} height {} ".format(width, height))


class Circle(Shape):
    num = 0
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        Circle.num += 1

    def set_radius(self, radius):
        self.radius = radius

    @classmethod
    def get_num_circles(cls):
        return cls.num

    def draw(self):
        print("Drawing a circles with {}".format(self.radius))


class Rectangle(Shape):
    num = 0
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        Rectangle.num += 1

    def set_width(self):
        self.width = width

    def set_height(self):
        self.height = height

    def print_area(self):
        area = self.height * self.width
        print("Rectangles width {} height {} has area as {}".format(width, height, area))

    @classmethod
    def get_num_rectangles(cls):
        return cls.num


    def draw(self):
        print("Drawing a rectangles with width {} height {} ".format(width, height))



if __name__=="__main__":
    circles = []
    rectangles = []
    NUM_OBJECTS = 3
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(Circle(color, radius))
        circles[i].draw()
    print(f"Num circles is {Circle.get_num_circles()}")

    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        rectangles.append(Rectangle(color, width, height))
        rectangles[i].draw()
        rectangles[i].print_area()
    print(f"Num rectangles is {Rectangle.get_num_rectangles()}")
