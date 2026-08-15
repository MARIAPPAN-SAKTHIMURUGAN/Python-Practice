import copy


def list_slicing():
    numbers = [56, 67, 89, 90, 86, 34, 90]

    print("Original Numbers:", numbers)

    print("Slice with Start and Stop [0:2]:", numbers[0:2])
    print("Slice with Start [2:]:", numbers[2:])
    print("Slice with Stop [:4]:", numbers[:4])
    print("Slice with Step [::3]:", numbers[::3])

    print("Reverse Output [::-1]:", numbers[::-1])
    print("Reverse Output [::-2]:", numbers[::-2])

    copied_numbers = numbers[:]
    print("Copy Using Slicing:", copied_numbers)


def list_copy_and_deepcopy():
    numbers = [56, 67, 89, 90, 86, 34, 90]

    # Reference assignment
    reference_numbers = numbers
    reference_numbers.append(99)

    print("\nOriginal Numbers:", numbers)
    print("Reference Numbers:", reference_numbers)
    print("Changes made through reference also affect the original list.")

    # Shallow copy using copy()
    copied_numbers = numbers.copy()
    copied_numbers.append(50)

    print("\nOriginal Numbers:", numbers)
    print("Copied Numbers:", copied_numbers)
    print("Changes made to copied_numbers do not affect the original list.")

    # Shallow copy with nested lists
    nested_numbers = [
        [10, 20],
        [40, 50]
    ]

    shallow_copy = nested_numbers.copy()
    shallow_copy[0].append(30)

    print("\nOriginal Nested List:", nested_numbers)
    print("Shallow Copy:", shallow_copy)
    print("Nested changes are reflected in both lists.")

    # Deep copy
    deep_copy = copy.deepcopy(nested_numbers)
    deep_copy[0].append(60)

    print("\nOriginal Nested List:", nested_numbers)
    print("Deep Copy:", deep_copy)
    print("Nested changes in deep_copy do not affect the original list.")


# Function calls
list_slicing()
list_copy_and_deepcopy()
