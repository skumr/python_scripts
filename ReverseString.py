def revString():
    string = input("Please enter a sentence:")
    rev_String = ''
    count = len(string)

    while count > 0:
        for i in range(len(string)):
            rev_String += string[count - 1]
            count -= 1
    print(rev_String)