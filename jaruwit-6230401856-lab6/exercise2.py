numbers = (2, 123.4567, 10000, 12345.67)
print("file_{:03d}:".format(numbers[0]), "{:2.2f},".format(numbers[1]),
      "{:3.2e}".format(numbers[2]),
      "{:3.2e}".format(numbers[3]))
