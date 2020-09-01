def robust_calculator():
    try:
        number1 = input("Please enter the first operand ('q to quit'):")
        if not number1:
            raise ValueError("Please enter a number")
        if number1.lower() == "q":
            quit()
        number1 = float(number1)
        number2 = input("Please enter the second operand ('q to quit'):")
        if not number2:
            raise ValueError("Please enter a number")
        if number2.lower() == "q":
            quit()
        number2 = float(number2)
        operation = input("Enter an operation ('+', '-', '*', '/'):")
        if operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "":
            print("Operation must be ADD, SUB, MUL, or DIV.")
            robust_calculator()
        user_format = input("Enter output format (float, int):")
        if user_format.lower() == "float" or user_format == "":
            if operation == "+" or operation == "":
                sum_plus = number1 + number2
                print("{} + {} = {}".format(number1, number2, sum_plus))
            if operation == "-":
                sum_minus = number1 - number2
                print("{} - {} = {}".format(number1, number2, sum_minus))
            if operation == "*":
                sum_multi = number1 * number2
                print("{} * {} = {}".format(number1, number2, sum_multi))
            if operation == "/":
                sum_divide = number1 / number2
                print("{} / {} = {}".format(number1, number2, sum_divide))
        if user_format.lower() == "int":
            if operation == "+" or operation == "":
                sum_plus = number1 + number2
                sum_plus = int(round(sum_plus))
                print("{} + {} = {}".format(number1, number2, sum_plus))
            if operation == "-":
                sum_minus = number1 - number2
                sum_minus = int(round(sum_minus))
                print("{} - {} = {}".format(number1, number2, sum_minus))
            if operation == "*":
                sum_multi = number1 * number2
                sum_multi = int(round(sum_multi))
                print("{} * {} = {}".format(number1, number2, sum_multi))
            if operation == "/":
                sum_divide = number1 / number2
                sum_divide = int(round(sum_divide))
                print("{} / {} = {}".format(number1, number2, sum_divide))
        robust_calculator()


    except ValueError:
        print("Please enter a number")
        robust_calculator()
    except ZeroDivisionError:
        print("Cannot divide by zero")
        print("We cannot perform your requested calculation.")
        robust_calculator()
robust_calculator()