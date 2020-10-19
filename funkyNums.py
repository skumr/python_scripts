"""
This module contains one function: funkyNums, which takes one parameter: n, a positive integer.

Name: Sudarshan Kumar
Student #: 20182908

"""

"""
The function funkyNums that accepts a single parameter: n, a positive integer
and writes the provided integer to the console backwards.
"""


def funkyNums(n):
    if n <= 0:
        return "Enter non-zero, positive num"
    elif n < 10:
        return n
    else:
        revNum = str(n % 10) + str(funkyNums(n // 10))
        return revNum


if __name__ == "__main__":
    n = 0
    print(funkyNums(n))  # check for 0 base case, will return statement
    n = -9
    print(funkyNums(n))  # check for negative number base case, will return statement

    for i in range(1, 10):
        print(funkyNums(i))  # check for second base case for all numbers < 10,
        # returns n if n < 10 (cannot flip single digit)

    n = 19
    print(funkyNums(n))  # for n, funkyNums returns 91
    n = 78
    print(funkyNums(n))  # for n, funkyNums returns 87
    n = 90
    print(funkyNums(n))  # for n, funkyNums returns 09

    n = 763
    print(funkyNums(n))  # for n, funkyNums returns 367
    n = 923
    print(funkyNums(n))  # for n, funkyNums returns 329

    # Assignment test case
    n = 5637
    print(funkyNums(n))  # for n, funkyNums returns 7365
