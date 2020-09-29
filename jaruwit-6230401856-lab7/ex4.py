class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls, num):
        cls.num = num
        divided = (cls.num / 2)
        return "Factors of {} is {} and {}".format(cls.num, divided, divided)

    @staticmethod
    def is_valid_divisor(arg):
        if arg == 0:
            return "{} is not a valid divisor".format(arg)
        else:
            return "{} is a valid divisor".format(arg)

    def display(self):
        return self.x, self.y


if __name__ == "__main__":
    print("3 + 5 is", Numbers(3, 5).add())
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(8))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
