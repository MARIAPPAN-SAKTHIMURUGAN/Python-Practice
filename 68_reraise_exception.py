def fiber_validation(length):

    try:

        length = float(length)

        if length <= 0:
            raise ValueError("Fiber length must be greater than zero")

        return length

    except ValueError as e:

        print("Fiber validation error:", e)

        raise


try:

    length = fiber_validation("-500")

    print("Fiber length:", length)

except ValueError:

    print("Main program received the error")
