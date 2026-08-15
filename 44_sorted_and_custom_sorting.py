def sort_numbers():
    numbers = [50, 10, 40, 20, 30]

    sorted_numbers = sorted(numbers)
    descending_numbers = sorted(numbers, reverse=True)

    print("Original Numbers:", numbers)
    print("Sorted Numbers:", sorted_numbers)
    print("Descending Numbers:", descending_numbers)


def get_name_length(name):
    return len(name)


def get_salary(employee):
    return employee["salary"]


def sort_employees_with_lambda():
    employees = [
        ("Arun", 50000),
        ("Bala", 70000),
        ("Kumar", 40000),
        ("Ravi", 60000)
    ]

    sorted_by_name = sorted(employees, key=lambda employee: employee[0])
    sorted_by_salary = sorted(employees, key=lambda employee: employee[1])

    print("Lambda - Sorted by Name:", sorted_by_name)
    print("Lambda - Sorted by Salary:", sorted_by_salary)


def sort_dictionary():
    employees = [
        {"name": "Arun", "salary": 50000},
        {"name": "Bala", "salary": 70000},
        {"name": "Kumar", "salary": 40000}
    ]

    sorted_by_salary = sorted(
        employees,
        key=lambda employee: employee["salary"]
    )

    sorted_by_salary_descending = sorted(
        employees,
        key=get_salary,
        reverse=True
    )

    print("Dictionary - Sorted by Salary:", sorted_by_salary)
    print("Dictionary - Function + Reverse:", sorted_by_salary_descending)


# Sorting strings by length
names = ["Raj", "Alexander", "John", "Christopher"]

sorted_by_length = sorted(names, key=len)
sorted_by_length_descending = sorted(
    names,
    key=get_name_length,
    reverse=True
)

print("Direct key=len:", sorted_by_length)
print("Custom Function:", sorted_by_length_descending)


# Function calls
sort_numbers()
sort_employees_with_lambda()
sort_dictionary()
