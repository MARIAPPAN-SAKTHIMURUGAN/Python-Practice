def set_operations():
    # List containing duplicate values
    numbers_list = [10, 20, 30, 40, 40, 50, 50, 70]

    # Set automatically removes duplicates
    numbers = {10, 20, 30, 40, 40, 50, 50, 70}

    print("Original List:", numbers_list)
    print("Set - Duplicates Removed:", numbers)

    # Add an element
    numbers.add(1000)
    print("After add(1000):", numbers)

    # Remove an existing element
    numbers.remove(50)
    print("After remove(50):", numbers)

    # Discard a non-existing element
    numbers.discard(80)
    print("After discard(80):", numbers)

    # Sorted set
    print("Sorted Set:", sorted(numbers))

    # Empty set
    empty_set = set()
    print("Empty Set:", empty_set)
    print("Type:", type(empty_set))

    # Two sets
    numbers_set1 = {10, 20, 30}
    numbers_set2 = {30, 40, 50, 60}

    # Union
    union_result = numbers_set1 | numbers_set2
    print("\nUnion:", union_result)

    # Intersection
    intersection_result = numbers_set1 & numbers_set2
    print("Intersection:", intersection_result)

    # Difference
    difference_set1 = numbers_set1 - numbers_set2
    print("Difference (set1 - set2):", difference_set1)

    difference_set2 = numbers_set2 - numbers_set1
    print("Difference (set2 - set1):", difference_set2)

    # Symmetric Difference
    symmetric_difference = numbers_set1 ^ numbers_set2
    print("Symmetric Difference:", symmetric_difference)

    # Remove duplicate fiber IDs
    fiber_ids = [
        "F001",
        "F002",
        "F001",
        "F003",
        "F002",
        "F004"
    ]

    unique_fibers = set(fiber_ids)

    print("\nOriginal Fiber IDs:", fiber_ids)
    print("Unique Fiber IDs:", unique_fibers)


set_operations()
