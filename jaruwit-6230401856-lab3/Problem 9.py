def numbers():
    correct = False
    while not correct:
        try:
            numbers = int(input("Enter an interger:"))
            if numbers % 2 == 1:
                pass
            if numbers % 2 == 0:
                print(numbers)
            if numbers == 99:
                break
        except ValueError:
            print("Invalid")
numbers()

