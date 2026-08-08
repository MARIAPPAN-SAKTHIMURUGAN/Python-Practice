# Find the first non-repeating number

def first_non_repeating(numbers):

    storage = {}

    # Count occurrences
    for num in numbers:

        if num in storage:
            storage[num] += 1
        else:
            storage[num] = 1

    # Find first number with frequency 1
    for num in numbers:

        if storage[num] == 1:
            return num

    return None


numbers = [23, 23, 56, 56, 89, 98]

print("First non-repeating:", first_non_repeating(numbers))
