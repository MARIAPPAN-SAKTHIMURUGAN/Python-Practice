# Reverse a string without using reversed() or slicing

def reverse(value):

    result = ""

    for ch in value:
        result = ch + result

    return result


value = "Python"

print("Original:", value)
print("Reversed:", reverse(value))
