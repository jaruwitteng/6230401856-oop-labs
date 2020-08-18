def find_average():
    correct = False
    while not correct:
        try:
            x = 0
            loop = [1]
            sum = 0
            for x in loop:
                digit = int(input("Enter an integer:"))
                if digit > 0:
                    loop.append(x + 1)
                    sum += digit
                if digit < 0 and x == 1:
                    print("You haven't entered a positive number")
                    break
                if digit < 0 and x != 1:
                    average = sum / (x - 1)
                    print("Average is", average)
                    correct = True
                    break
        except ValueError:
            print("Invalid")
find_average()


