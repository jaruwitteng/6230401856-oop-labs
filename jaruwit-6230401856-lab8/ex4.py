class ComEnStudent:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def take_courses(self, *courses):
        for x in courses:
            self.courses.append(x)


    def __str__(self):
        return f"{self.name} has taken courses {self.courses}"


class CoEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)
        self.courses = courses


class DMEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)
        self.courses = courses

    def make_content_type(self, *special_courses):
        self.special_courses = special_courses

    def __str__(self):
        word = super().__str__()
        return f"{word}\nspecialized in creating content type:{self.special_courses}"

if __name__ == "__main__":
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN11302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)
