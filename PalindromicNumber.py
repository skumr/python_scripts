def numPal(x: int):
    new_num = str(x)
    nlist = [int(i) for i in new_num]
    rlist = list(reversed(nlist))

    if nlist == rlist:
        print(x, "is a Palindrome number.")
    else:
        print(x, "is not a Palindrome number.")