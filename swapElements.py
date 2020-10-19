"""
This function accepts a list of integers (intList) as its parameter
and returns a copy of the list in which neighboring elements have been swapped.
If the length of the list is odd, your function doesn't need to swap the last element -
this element can remain in its original position.
If the list is empty, return an empty list.

"""


def swapElements(intList, i=0):
    if i >= len(intList) - 1:
        return intList  # this will return the list if it is empty

    intList[i], intList[i + 1] = intList[i + 1], intList[i]
    return swapElements(intList, i + 2)  # recurs for the next two elements


if __name__ == "__main__":
    # test for special case (empty list)
    intList = []
    print(swapElements(intList))  # will return empty list back to console

    # test for special case (nested empty list)
    intList = [[]]
    print(swapElements(intList))  # will return nested empty list

    # test for special case (nested list with integers)
    intList = [[3, 8], [2, 1]]
    print(swapElements(intList))  # will return list of swapped elements [[2,1],[3,8]]

    # proves function swaps main list elements only

    # test case for lists of odd length, swap every pair but last element
    intList = [5, 9, 1]
    print(swapElements(intList))  # will return [9, 5, 1] <-- last element not swapped
    intList = [7, 9, 3, 1, 4, 0, 5]
    print(swapElements(intList))  # will return [9, 7, 1, 3, 0, 4, 5] <-- last element not swapped

    # test case for lists of even length, swap every pair of elements
    intList = [2, 0]
    print(swapElements(intList))  # will return [0, 2]
    intList = [5, 6, 9, 1]
    print(swapElements(intList))  # will return [6, 5, 1, 9]

    # run for assignment test case
    intList = [3, 8, 2, 1]
    print(swapElements(intList))  # will return [8, 3, 2, 1]
