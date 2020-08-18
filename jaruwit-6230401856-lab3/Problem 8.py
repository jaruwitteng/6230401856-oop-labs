def print_numbers():
    correct = False
    while not correct:
        try:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            numbers_string = [str(number) for number in numbers]
            print("|".join(numbers_string))
            correct = True
            break
        except ValueError:
            print("Invalid")
print_numbers()