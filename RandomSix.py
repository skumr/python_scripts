import random


def randomSix():
    num_list = []
    final_list = []

    for i in range(1, 1501):
        if i % 5 == 0:
            if i % 7 == 0:
                num_list.append(i)

    for i in range(6):
        final_list.append(random.choice(num_list))

    print(final_list)
