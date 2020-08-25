def calculator():
    correct = False
    while not correct:
        try:
            number1 = int(input("Please enter the first operand:"))
            correct = True
        except ValueError:
            print("Please enter a number")
    while correct:
        try:
            number2 = int(input("Please enter the second operand:"))
            correct = False
        except ValueError:
            print("Please enter a number")
    while not correct:
        try:
            operators = input("Please enter an operator (+,-,*,/):")
            if operators == "+" or operators == "-" or operators == "*" or operators == "/":
                number1 = int(number1)
                number2 = int(number2)
                if operators == "+":
                    answer_plus = number1 + number2
                    print("Result of", number1, operators, number2, "is", answer_plus)
                if operators == "-":
                    answer_minus = number1 - number2
                    print("Result of", number1, operators, number2, "is", answer_minus)
                if operators == "*":
                    answer_divide = number1 * number2
                    print("Result of", number1, operators, number2, "is", answer_divide)
                if operators == "/":
                    answer_multiply = number1 / number2
                    print("Result of", number1, operators, number2, "is", answer_multiply)
                break
            else:
                print("Unknown operator")
        except ZeroDivisionError:
            print("Please don't divide by zero")
            calculator()
calculator()