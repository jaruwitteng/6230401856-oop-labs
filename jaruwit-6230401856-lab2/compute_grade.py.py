def check():
    name = input("Please enter student name :")
    correct_answer = False
    while not correct_answer:
        try:
            midterm_score = int(input("Please enter the student's midterm exam mark :"))
            if midterm_score >= 101 or midterm_score <= -1:
                print("Please enter valid exam mark")
                check()
            final_score = int(input("Please enter the student's final exam mark :"))
            if final_score >= 101 or final_score <= -1:
                print("Please enter valid exam mark")
                check()
            score = (final_score + midterm_score) / 2
            if score < 50:
                print(name, "has total mark at", score, "and graded as F")
            elif score <= 60:
                print(name, "has total mark at", score, "and graded as D")
            elif score <= 70:
                print(name, "has total mark at", score, "and graded as C")
            elif score <= 80:
                print(name, "has total mark at", score, "and graded as B")
            elif score <= 100:
                print(name, "has total mark at", score, "and graded as A")
        except ValueError:
            print("Please enter valid mark")
        else:
            correct_answer = True

check()
