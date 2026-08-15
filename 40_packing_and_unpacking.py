def add(*numbers):
    return sum(numbers)


def packing_unpacking():
    numbers = (56, 89, 78)

    print("Original Values:", numbers)
    print("Unpacking Values:", *numbers)

    list1 = [10, 20, 30]
    list2 = [40, 50, 60]

    print("Original Lists:", list1, list2)
    print("Unpacking Lists:", *list1, *list2)

    result = add(*numbers)
    print("Sum of Numbers:", result)


def add_numbers(*args):
    print("Args Output:", args)


def combine_employee_details():
    employees = [
        {"name": "Mari", "salary": 50000},
        {"name": "Mupp", "salary": 60000},
        {"name": "Kali", "salary": 55000},
        {"name": "Utchimahali", "salary": 70000}
    ]

    details = [
        {"city": "Tirunelveli", "experience": 10},
        {"city": "Tirunelveli Town", "experience": 13},
        {"city": "Pilayarkulam", "experience": 14},
        {"city": "Pilayarkulam", "experience": 15}
    ]

    print("Employee Details:", employees)
    print("Additional Details:", details)

    combined_data = [
        {**employee, **detail}
        for employee, detail in zip(employees, details)
    ]

    print("Combined Employee Details:")

    for data in combined_data:
        print(data)


# Function calls
add_numbers(10, 20, 30, 40)
packing_unpacking()
combine_employee_details()
