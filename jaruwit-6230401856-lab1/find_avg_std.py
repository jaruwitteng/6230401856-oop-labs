import random
number1 = (random.randint(1, 10))
number2 = (random.randint(1, 10))
average = (number1 + number2) / 2
standard = (((number1 - average) ** 2 + (number2 - average) ** 2) / 2) ** 0.5
standard = abs(standard)
print("The average of", number1, "and", number2, "is", average)
print("The standard deviation of", number1, "and", number2,  "is", standard)
