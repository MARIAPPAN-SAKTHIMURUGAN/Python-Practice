# Count how many times a number appears

def count_numbers(numbers, find):

    count_no = 0

    for no in numbers:

        if no == find:
            count_no += 1

    return count_no


numbers = [88, 10, 10, 99, 99, 77, 88, 10, 77]

print("10 appears:", count_numbers(numbers, 10), "times")
