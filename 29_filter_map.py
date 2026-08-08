def greater_than_20(x):
    return x > 20


def multiply_by_two(x):
    return x * 2


def filter_map_example():
    numbers = (10, 15, 20, 25, 30, 35, 40)

    # Filter + Map with normal functions
    result = map(
        multiply_by_two,
        filter(greater_than_20, numbers)
    )

    print("Filter + Map:", list(result))

    # For loop
    result1 = []

    for num in numbers:
        if num > 20:
            result1.append(num * 2)

    print("For loop:", result1)

    # Filter + Map with Lambda
    result2 = map(
        lambda x: x * 2,
        filter(lambda x: x > 20, numbers)
    )

    print("Filter + Map with Lambda:", list(result2))


filter_map_example()
