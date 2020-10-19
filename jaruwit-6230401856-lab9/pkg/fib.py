def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n - 2) + fib(n - 1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(fib(int(sys.argv[1])))






