class Student:
    university_name = "Khon Kaen University"

    def __init__(self, name, *course):
        self.name = name
        self.course = course

    def print(self):
        print("{} registered courses {}".format(self.name, self.course))


if __name__ == "__main__":
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    print("These students are in", Student.university_name)
