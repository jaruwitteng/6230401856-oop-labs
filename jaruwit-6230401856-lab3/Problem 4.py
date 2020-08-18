def factorial():
    correct = False
    while not correct:
        try:
            digit = int(input("Enter a number to find the factorial:"))
            total = 1
            for digit in range(1, digit + 1):
                total *= digit
            print("Factorial of", digit, "is", total)
            correct = True
        except ValueError:
            print("Invalid")
factorial()
