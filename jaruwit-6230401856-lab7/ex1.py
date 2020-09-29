class Student:
    def __init__(self, name, *course):
        self.name = name
        self.course = course


if __name__ == "__main__":
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    print(manee.name, "registered courses", manee.course)
    print(mana.name, "registered courses", mana.course)
    print(chujai.name, "registered courses", chujai.course)
