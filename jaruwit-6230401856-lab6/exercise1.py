numbers = (2, 10, 11, 3)
numbers_2 = []
print("{:30s}".format("Input filenames are"), numbers)
for x in numbers:
    numbers_2.append("file_{:04d}".format(x))

print("{:30s}".format("zero padded filenames"), numbers_2)
numbers_2.sort()
print("{:30s}".format("sorted filenames are"), numbers_2)
