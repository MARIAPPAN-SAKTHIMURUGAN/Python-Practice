def greater_than_20(x):
    return x > 20


def filter_example():
    numbers = (10, 15, 20, 25, 30, 35, 40)

    # Filter with normal function
    result = filter(greater_than_20, numbers)

    print("Filter with Function:", list(result))

    # For loop
    result1 = []

    for num in numbers:
        if num > 20:
            result1.append(num)

    print("For loop:", result1)

    # Filter with lambda
    result2 = filter(lambda x: x > 20, numbers)

    print("Filter with Lambda:", list(result2))


filter_example()
