def text():
    try:
        with open("fiber_data.csv", "r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print("Fiber data file not found")

    finally:
        print("File processing completed")


def validate_fiber():

    try:
        length = int(input("Enter Fiber Length: "))

        if length <= 0:
            raise ValueError("Fiber length not valid")

    except ValueError as e:
        print("Error:", e)

    else:
        km = length / 1000
        print("Length in Km:", km)

    finally:
        print("Fiber validation completed")


text()
validate_fiber()
