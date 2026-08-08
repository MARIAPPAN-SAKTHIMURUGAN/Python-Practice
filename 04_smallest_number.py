# Find the smallest number in a list

def smallest(numbers):
    smallest_no = numbers[0]

    for no in numbers:
        if no < smallest_no:
            smallest_no = no

    return smallest_no


numbers = [15, 4, 22, 8]

print("Smallest:", smallest(numbers))
