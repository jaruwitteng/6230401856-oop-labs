import random
import statistics
number1 = (random.randint(1, 10))
number2 = (random.randint(1, 10))
average = (number1 + number2)/2
numbers_store = [number1, number2]
std = (statistics.stdev(numbers_store))
print("The average of", number1, "and", number2, "is", average)
print("The standard deviation of", number1, "and", number2,  "is", std%2)
