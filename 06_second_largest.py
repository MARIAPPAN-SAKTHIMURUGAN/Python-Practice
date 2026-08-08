# Find the second largest number

def second_largest(numbers):

    first_largest = float("-inf")
    second_largest = float("-inf")

    for no in numbers:

        if no > first_largest:
            second_largest = first_largest
            first_largest = no

        elif no > second_largest and no != first_largest:
            second_largest = no

    return second_largest


numbers = [10, 25, 5, 40]

print("Second Largest:", second_largest(numbers))
