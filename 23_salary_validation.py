class InvalidSalaryError(Exception):
    pass


def salary_check():
    try:
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        grade = input("Enter designation: ")

        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative")

        if not name.isalpha():
            raise ValueError("Name must contain only characters")

    except InvalidSalaryError as error:
        print("Salary Error:", error)

    except ValueError as error:
        print("Input Error:", error)

    else:
        print(f"Name: {name}")
        print(f"Salary: {salary}")
        print(f"Designation: {grade}")

    finally:
        print("Salary check completed")


salary_check()
