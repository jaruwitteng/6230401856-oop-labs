class Rectangle:

    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def __str__(self):
        return "This rectangle has width as {} height as {}".format(self.__width, self.__height)


if __name__ == "__main__":
    rect1 = Rectangle(3, 4)
    print(rect1)
    print("Width is {}".format(rect1.get_width()))
    rect1.set_height(5)
    print("Height is {}".format(rect1.get_height()))
