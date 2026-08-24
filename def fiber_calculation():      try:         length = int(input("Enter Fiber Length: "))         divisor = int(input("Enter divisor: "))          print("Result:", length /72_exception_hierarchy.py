def fiber_calculation():

    try:
        length = int(input("Enter Fiber Length: "))
        divisor = int(input("Enter divisor: "))

        print("Result:", length / divisor)

    except ValueError:
        print("Please enter a valid number")

    except ZeroDivisionError:
        print("Divisor must not be zero")


fiber_calculation()
