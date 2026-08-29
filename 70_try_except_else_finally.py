def fiber_calculation():

    try:

        length = int(input("Enter Fiber Length: "))
        cores = int(input("Enter Number of Cores: "))

        if length <= 0:
            raise ValueError("Fiber length must be greater than zero")

        if cores <= 0:
            raise ValueError("Number of cores must be greater than zero")

    except ValueError as e:

        print("Error:", e)

    else:

        print("Fiber Length:", length, "meters")
        print("Fiber Length:", length / 1000, "KM")
        print("Number of Cores:", cores)

    finally:

        print("Fiber calculation completed")


fiber_calculation()
