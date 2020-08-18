def months():
    x = 0
    correct = False
    while not correct:
        try:
            if x == 0:
                months = (
                    "January", "February", "March",
                    "April", "May", "June",
                    "July", "August", "September",
                    "October", "November", "December"
                )
                days = ("31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31")
                months_and_days = list(zip(months, days))
                months_and_days = dict(months_and_days)
                print(months_and_days.items())
                user_input = input("Enter month:")
                print("Number of days in", user_input, "is", months_and_days[user_input])
                break
        except KeyError:
            print("Invalid")
        else:
            correct = True

months()