def addNext(n):
    if n == 1:
        return n

    elif n == 0:
        return n

    else:
        return n + addNext(n - 2)


if __name__ == "__main__":
    # test case for base case
    n = 1
    print(addNext(n))  # will return 1

    # test case for second base case
    n = 0
    print(addNext(n))  # will return 0

    # test for single digit numbers
    n = 2
    print(addNext(n))  # will return 2

    # test case for assignment example
    n = 6
    print(addNext(n))  #
