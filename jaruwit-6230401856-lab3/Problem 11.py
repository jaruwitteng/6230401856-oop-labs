def calculator():
    correct = False
    while not correct:
        try:
            number_one = (input("Enter the first number:"))
            if number_one.lower() == "quit":
                break
            number_two = (input("Enter the second number:"))
            if number_two.lower() == "quit":
                break
            operator = input("Enter the operator:")
            if operator != "+" and operator != "-" and operator != "*" and operator != "/":
                print("Unknown operator")
                break
            if operator == "/" and number_two == "0":
                print("Cannot divide a number by 0")
                break
            number_one = int(number_one)
            number_two = int(number_two)
            if operator == "+":
                plus = number_one + number_two
                print(number_one, "+",number_two, "=", plus)
            if operator == "-":
                minus = number_one - number_two
                print(number_one, "-", number_two, "=", minus)
            if operator == "*":
                multiply = number_one * number_two
                print(number_one, "*", number_two, "=", multiply)
            if operator == "/":
                divide = number_one / number_two
                print(number_one, "/", number_two, "=", divide)
        except ValueError:
            print("Invalid")
        else:
            correct = True

calculator()