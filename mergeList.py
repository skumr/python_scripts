

def mergeList(nestedLis):
    if not nestedLis:
        return nestedLis

    if isinstance(nestedLis[0], list):
        return mergeList(nestedLis[0]) + mergeList(nestedLis[1:])

    return nestedLis[:1] + mergeList(nestedLis[1:])


if __name__ == "__main__":

    # test for base case
    nestedLis = [[]]
    print(mergeList(nestedLis))  # will return None

