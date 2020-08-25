final_list = []
numbers = input("Enter the list of numbers (delimited by comma):")
seperate_numbers  = numbers.split(",")
print(seperate_numbers)

try:
    final_list = int(input("Enter an index: "))
    print(seperate_numbers[final_list])
except IndexError:
    print("The list has no element at index", final_list)