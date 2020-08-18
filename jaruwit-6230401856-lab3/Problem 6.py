def months_and_days():
    correct = False
    while not correct:
        try:
            months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December")
            days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            dict = {}
            for d, m in enumerate(months):
                dict[m] = days[d]
            print(dict.items())
            month_input = input("Enter month:")
            print("Number of days in", month_input, "is", dict[month_input])
            correct = True
        except KeyError:
            print("Invalid")
months_and_days()