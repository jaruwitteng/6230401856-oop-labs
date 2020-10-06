class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("I'm", self.name)

    def move(self):
        pass


class Cat(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name)
        self.owner = owner
        self.color = color

    def show_info(self):
        print("I'm", self.name,
              "\n and is", self.color,
              "\n belonging to", self.owner)

    def move(self):
        print("Cat likes to walk more than run")


class Dog(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name)
        self.owner = owner
        self.color = color

    def show_info(self):
        print("I'm", self.name,
              "\n and is", self.color,
              "\n belonging to", self.owner)

    def move(self):
        print("Dog likes to run more than walk")

    def eat_cat(self, name):
        print("Dog", self.name, "eats cat", name.name)


if __name__ == "__main__":
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "White")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)
