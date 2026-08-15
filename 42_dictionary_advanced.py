def dictionary_basic_operations():
    employee = {
        "name": "Mupp",
        "salary": 50000,
        "city": "Chennai"
    }

    print("Original Dictionary:", employee)

    # get()
    print("City using get():", employee.get("city"))

    # Add new key
    employee["experience"] = 10
    print("After Adding Experience:", employee)

    # Update value
    employee["salary"] = 60000
    print("After Salary Update:", employee)

    # Delete key
    del employee["city"]
    print("After Deleting City:", employee)

    # clear()
    employee.clear()
    print("After Clear:", employee)


def nested_dictionary_operations():
    employees = {
        "E001": {
            "name": "Mupp",
            "salary": 50000
        },
        "E002": {
            "name": "Mari",
            "salary": 50080
        },
        "E003": {
            "name": "Utchimahali",
            "salary": 55000
        },
        "E004": {
            "name": "Thadiveeran",
            "salary": 60000
        },
        "E005": {
            "name": "Kali",
            "salary": 70000
        },
        "E006": {
            "name": "Nellaipar",
            "salary": 65000
        },
        "E007": {
            "name": "Kandimathi",
            "salary": 65000
        }
    }

    # Add new value
    employees["E001"]["experience"] = 17

    # Update existing value
    employees["E002"]["salary"] = 80000

    # update()
    employees["E003"].update({
        "salary": 70000,
        "city": "Tirunelveli-Town"
    })

    print("\nUpdated E001:", employees["E001"])
    print("Updated E002:", employees["E002"])
    print("Updated E003:", employees["E003"])

    # pop()
    removed_city = employees["E003"].pop("city")
    print("Removed City:", removed_city)
    print("E003 After pop():", employees["E003"])

    # values()
    print("\nValues Output:")
    for employee in employees.values():
        print(employee)

    # keys()
    print("\nKeys Output:")
    for employee_id in employees.keys():
        print(employee_id)

    # items()
    print("\nItems Output:")
    for employee_id, employee in employees.items():
        print("ID:", employee_id)
        print("Name:", employee["name"])
        print("Salary:", employee["salary"])

    # Nested get()
    print(
        "\nE002 Name:",
        employees.get("E002", {}).get("name", "Name Not Available")
    )

    print(
        "E003 City:",
        employees.get("E003", {}).get("city", "City Not Available")
    )

    print(
        "Unknown Employee:",
        employees.get("E999", {}).get("name", "Employee Not Available")
    )


def dictionary_merging():
    employee = {
        "name": "Mupp",
        "salary": 50000
    }

    details = {
        "city": "Chennai",
        "experience": 10
    }

    # Dictionary unpacking
    merged_dictionary = {
        **employee,
        **details
    }

    print("\nDictionary using **:")
    print(merged_dictionary)

    # Dictionary | operator
    merged_dictionary_2 = employee | details

    print("\nDictionary using |:")
    print(merged_dictionary_2)

    # Dictionary |= operator
    employee_copy = employee.copy()
    employee_copy |= details

    print("\nDictionary using |=:")
    print(employee_copy)


# Function calls
dictionary_basic_operations()
nested_dictionary_operations()
dictionary_merging()
