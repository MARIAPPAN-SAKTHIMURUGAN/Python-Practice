def tuple_operations():
    numbers = (2, 1, 4, 67, 56, 13, 13, 56)

    print("Original Tuple:", numbers)

    # Tuple Indexing
    print("\n--- Tuple Indexing ---")
    print("Index 0:", numbers[0])
    print("Index 2:", numbers[2])
    print("Last Element:", numbers[-1])
    print("Second Last Element:", numbers[-2])

    # Tuple Slicing
    print("\n--- Tuple Slicing ---")
    print("numbers[0:1]:", numbers[0:1])
    print("numbers[0:2]:", numbers[0:2])
    print("numbers[:3]:", numbers[:3])
    print("numbers[:5:2]:", numbers[:5:2])
    print("Reverse:", numbers[::-1])

    # Tuple Methods
    print("\n--- Tuple Methods ---")
    print("Count of 13:", numbers.count(13))
    print("First Index of 13:", numbers.index(13))

    # Tuple Packing
    print("\n--- Tuple Packing ---")
    employee = "Arun", 50000, "Chennai"
    print("Packed Employee:", employee)

    # Tuple Unpacking
    print("\n--- Tuple Unpacking ---")
    name, salary, city = employee

    print("Name:", name)
    print("Salary:", salary)
    print("City:", city)

    # Extended Tuple Unpacking
    first_number, *middle_numbers, last_number = numbers

    print("\n--- Extended Tuple Unpacking ---")
    print("First:", first_number)
    print("Middle:", middle_numbers)
    print("Last:", last_number)

    # Swapping Variables
    print("\n--- Variable Swapping ---")

    first = 10
    last = 20

    print("Before Swapping:")
    print("First:", first)
    print("Last:", last)

    first, last = last, first

    print("After Swapping:")
    print("First:", first)
    print("Last:", last)

    # Nested Tuples
    employees = (
        ("E001", "Arun", 50000),
        ("E002", "Bala", 60000),
        ("E003", "Kumar", 70000)
    )

    print("\n--- Nested Tuples ---")

    print("E001 Salary:", employees[0][2])

    for employee_id, employee_name, salary in employees:
        print(
            "Employee ID:", employee_id,
            "| Name:", employee_name,
            "| Salary:", salary
        )


tuple_operations()
