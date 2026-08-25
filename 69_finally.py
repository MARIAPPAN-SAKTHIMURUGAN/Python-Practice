def fiber_processing():

    try:

        length = int(input("Enter Fiber Length: "))

        if length < 0:
            raise ValueError("Fiber length cannot be negative")

        print("Fiber Length:", length)
        print("Fiber processing successful")

    except ValueError as e:

        print("Error:", e)

    finally:

        print("Fiber processing completed")


fiber_processing()
