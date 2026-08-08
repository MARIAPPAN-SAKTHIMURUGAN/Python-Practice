from functools import reduce


def add(x, y):
    return x + y


def reduce_example():
    numbers = (10, 15, 20, 25, 30, 35, 40)

    result = reduce(add, numbers)

    print("Reduce Result:", result)


reduce_example()
