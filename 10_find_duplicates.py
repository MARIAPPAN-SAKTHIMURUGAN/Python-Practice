# Find duplicate numbers without using set() or Counter

def find_duplicates(numbers):

    frequency = {}

    # Count each number
    for num in numbers:

        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find numbers that appear more than once
    result = []

    for num in numbers:

        if frequency[num] > 1 and num not in result:
            result.append(num)

    return result


numbers = [88, 10, 10, 99, 99, 77, 88, 10, 77]

print("Duplicates:", find_duplicates(numbers))
