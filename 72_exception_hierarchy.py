def fiber_calculation():

    try:
        length = int(input("Enter Fiber Length: "))

        print("Fiber length in KM:", length / 1000)

    except ValueError:
        print("Please enter a valid number")

    except ZeroDivisionError:
        print("Number must not be zero")


fiber_calculation()
