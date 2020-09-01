def factorial(digit):
        if digit < 0:
            print("Please enter a positive integer. {} is not a positive integer".format(digit))
            quit()
        if digit == 0:
            print("factorial(0) is 1")
            quit()
        if digit == 1:
            return 1
        else:
            return (digit * factorial(digit - 1))


try:
    digit = int(input("Enter an integer:"))
    print("factorial({}) is {}".format(digit, factorial(digit)))
except ValueError as err:
    print("Please enter a positive integer.%s" % err )
