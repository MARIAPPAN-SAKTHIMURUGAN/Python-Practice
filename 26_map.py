def double(x):
    return x * 2


def map_example():
    numbers = (10, 20, 30, 40, 50)

    # For loop
    result = []

    for num in numbers:
        result.append(num * 2)

    print("For loop Result:", result)

    # Map with lambda
    result1 = map(lambda x: x + 2, numbers)

    print("Map with Lambda:", list(result1))

    # Map with normal function
    result2 = map(double, numbers)

    print("Map with Function:", list(result2))


map_example()
