class InvalidFiberLengthError(Exception):
    pass


class InvalidSplitterRatioError(Exception):
    pass


def validate_fiber(length, splitter):

    if length <= 0:
        raise InvalidFiberLengthError(
            "Fiber length must be greater than zero"
        )

    if splitter not in [2, 4, 8, 16, 32, 64]:
        raise InvalidSplitterRatioError(
            "Invalid splitter ratio"
        )

    print("Fiber data is valid")


try:

    length = int(input("Enter Fiber Length: "))
    splitter = int(input("Enter Splitter Ratio: "))

    validate_fiber(length, splitter)

except InvalidFiberLengthError as e:

    print("Fiber Length Error:", e)

except InvalidSplitterRatioError as e:

    print("Splitter Error:", e)

else:

    print("Validation successful")

finally:

    print("Fiber validation completed")
