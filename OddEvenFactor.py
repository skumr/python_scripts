def oddEvenFactors(x: int):
    number = x
    for i in range(2, number - 1):
        if number % i == 0:
            print(i)
            i += 1
    return