def any_all():
    numbers = (10, 56, 87, 90, 98)

    any_result = any(number % 2 == 0 for number in numbers)
    print("Any result:", any_result)

    all_result = all(number % 2 == 0 for number in numbers)
    print("All result:", all_result)


any_all()
