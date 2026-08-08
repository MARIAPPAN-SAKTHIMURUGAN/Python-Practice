class InvalidSalaryError(Exception):
    pass


try:
    salary = int(input("Enter salary: "))

    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative")

except InvalidSalaryError as error:
    print("Salary Error:", error)

else:
    print("Valid salary:", salary)

finally:
    print("Salary check completed")
