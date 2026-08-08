# Find the third largest number

def third_largest(numbers):

    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for no in numbers:

        if no > first:
            third = second
            second = first
            first = no

        elif no > second and no != first:
            third = second
            second = no

        elif no > third and no != second and no != first:
            third = no

    return third


numbers = [10, 25, 5, 40, 30]

print("Third Largest:", third_largest(numbers))
