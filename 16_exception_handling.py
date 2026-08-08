def exception_handling():
    try:
        number = int(input("Enter a number: "))
        result = 10 / number

    except ValueError as error:
        print("Error:", error)

    except ZeroDivisionError as error:
        print("Error:", error)

    else:
        print("Result:", result)

    finally:
        print("Calculation completed")


exception_handling()
