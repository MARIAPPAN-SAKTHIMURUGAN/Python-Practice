# Find the largest number in a list

def largest(numbers):
    largest_no = numbers[0]

    for no in numbers:
        if no > largest_no:
            largest_no = no

    return largest_no


numbers = [23, 56, 78, 999]

print("Largest:", largest(numbers))
