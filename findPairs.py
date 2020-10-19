"""This program finds all the permutations of pairs
of numbers that add up to 10. The program takes in 3 parameters:
'n': a number, and 2 fixed paramters, 'i'= 0, 'count' = 0. This program
returns the count of the number of pairs for an input number. """

def findPairs(n, i=0, count=0):
    nString = str(n)

    if n < 0:
        return "Number must be a non-negative integer"

    else:
        if len(nString) == 1:
            return count
        if len(nString) == 3:
            if i == len(nString) - 1:
                n = int(nString[1:])
                return count + findPairs(n)
            else:
                if int(nString[0]) + int(nString[i + 1]) == 10:
                    return count + findPairs(n, i + 1, count + 1)

                return count + findPairs(n, i + 1)
        else:
            if i == len(nString) - 1:
                n = int(nString[1:])
                return count + findPairs(n)
            else:
                if int(nString[0]) + int(nString[i + 1]) == 10:
                    return count + findPairs(n, i + 1, count + 1)

                return count + findPairs(n, i + 1)


if __name__ == "__main__":
    n = -1
    print(findPairs(n))  # will return statement

    n = 72
    print(findPairs(n))  # will return 0

    n = 7391
    print(findPairs(n))

    n = 73
    print(findPairs(n))

    n = 7645238
    print(findPairs(n))
