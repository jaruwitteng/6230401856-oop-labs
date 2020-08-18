def fruit():
    correct = False
    while not correct:
        try:
            list = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
            for number, letter in enumerate(list):
                print("%d. %s" % (number+1, letter))
            correct = True
            break
        except ValueError:
            print("Invalid")
fruit()