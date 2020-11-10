from functools import reduce
import sys

class factorial():
    number = int(sys.argv[1])
    setnumbers = range(1, number+1)
    setnumbers = list(setnumbers)
    fac = list(map(lambda x: reduce(lambda x, y: x * y, range(1, x + 1)), setnumbers))
    print("With the argument of {}, the input list is {}".format(number, setnumbers))
    print("The factorial numbers are {}".format(fac))



if __name__ == '__main__':
    factorial()