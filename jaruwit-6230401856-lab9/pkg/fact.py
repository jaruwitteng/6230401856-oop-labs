def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))