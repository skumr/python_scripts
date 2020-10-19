def q9(x, y):
    dimList = [[] for i in range(x)]
    for i in range(len(dimList)):
        for j in range(y):
            dimList[i].append(i * j)

    print(dimList)