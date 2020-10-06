class Vehicle:
    def __init__(self, name, __speed, mileage):
        self.name = name
        self.__speed = __speed
        self.mileage = mileage

    def set_speed(self, __speed):
        self.__speed = __speed

    def get_speed(self):
        return self.__speed

class Car(Vehicle):
    def __init__(self, name, __speed, mileage, doors):
        self.doors = doors
        super().__init__(name, __speed, mileage)

    def __str__(self):
        return ("Name: {} speed: {} mileage: {} num doors {}".format(self.name, self.get_speed(), self.mileage, self.doors))


class Bus(Vehicle):
    def __init__(self, name, __speed, mileage, doors):
        self.doors = doors
        super().__init__(name, __speed, mileage)

    def __str__(self):
        return ("Name: {} speed: {} mileage: {} capacity {}".format(self.name, self.get_speed(), self.mileage, self.doors))


if __name__ == "__main__":
    car = Car("Toyoya Vios", 90, 150000, 4)
    bus = Bus("Scool Volvo", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)



