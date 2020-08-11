four_positive = []
four_odd = []
for digit in range(1, 5):
    four_positive.append(digit)
for digit in range(1, 8):
    if digit % 2 != 0:
        four_odd.append(digit)
set_positive = set(four_positive)
set_odd = set(four_odd)
print("A is ", set_positive)
print("B is", set_odd)
set_sum = set_positive.union(set_odd)
print("A sum B is", set_sum)
set_duplicate = set_positive.intersection(set_odd)
set_interception = set_positive - set_duplicate
print("A - B is", set_interception)
set0to20 = []
for digit in range(0, 20):
    set0to20.append(digit)
print(set0to20)
set3to12 = []
for digit in range(3, 13):
    set3to12.append(digit)
print(set3to12)
set0to50 = []
for digit in range(1, 51):
    if digit % 3 == 2:
        set0to50.append(digit)
print(set0to50)
