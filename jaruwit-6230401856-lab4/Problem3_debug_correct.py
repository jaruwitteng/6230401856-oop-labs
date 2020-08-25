import sys
def divide(dividend, divisor):
    return dividend / divisor
def calculator():
    try:
        dividend = int(input("Please enter the dividend:"))
        if dividend < 0:
            print("Can't be negative")
            exit()
        divisor = int(input("Please enter the divisor:"))
        if divisor <= 0:
            print("Can't be negative or zero")
            exit()
        answer = divide(dividend, divisor)
        print('The answer is: {}'.format(answer))
    except ValueError:
        print("Enter numbers")

calculator()