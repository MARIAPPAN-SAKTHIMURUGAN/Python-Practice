def check_numbers():
    numbers = (10, 15, 20, 25, 30)

    result = [
        "Even" if num % 2 == 0 else "Odd"
        for num in numbers
    ]

    print("Numbers:", numbers)
    print("Result:", result)


check_numbers()
