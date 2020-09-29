class Student:
    def __init__(self, name, *course):
        self.name = name
        self.course = course

    def print(self):
        print("{} registered courses {}".format(self.name, self.course))

    @classmethod
    def set_university_name(cls, uni_name):
        cls.university = uni_name

    @classmethod
    def get_university_name(cls):
        return cls.university


if __name__ == "__main__":
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    Student.set_university_name("KKU")
    print("These students are in", mana.get_university_name())
