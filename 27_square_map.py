def square(x):
    return x * x


def square_map():
    numbers = (5, 10, 15, 20, 25)

    result = map(square, numbers)

    print("Square using Map:", list(result))


square_map()
