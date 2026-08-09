def generator_example():
    numbers = [10, 20, 30, 40, 50]

    result = (num * 2 for num in numbers)

    print("Generator:", result)

    for value in result:
        print(value)


generator_example()
