from functools import reduce
import sys

class factorial():
    number = int(sys.argv[1])
    fac_num = reduce(lambda x, y: x * y, range(1, number + 1))
    print("Factorial of ({}) is {}".format(number, fac_num))

if __name__ == '__main__':
    factorial()