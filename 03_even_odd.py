# Check whether a number is even or odd

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = 10

if is_even(number):
    print("Even")
else:
    print("Odd")
