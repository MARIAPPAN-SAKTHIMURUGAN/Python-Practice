import csv


def write_fiber_csv():

    fibers = [
        {
            "FiberID": "F001",
            "Length": 450,
            "Status": "Active"
        },
        {
            "FiberID": "F002",
            "Length": 950,
            "Status": "Dark"
        },
        {
            "FiberID": "F003",
            "Length": 780,
            "Status": "IPL"
        },
        {
            "FiberID": "F004",
            "Length": 1200,
            "Status": "Active"
        }
    ]

    with open("fiber_data.csv", "w", newline="") as file:

        fieldnames = ["FiberID", "Length", "Status"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(fibers)

    print("CSV file created successfully.")


def read_fiber_csv():

    print("\n--- Fiber CSV Data ---")

    with open("fiber_data.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            fiber_id = row["FiberID"]
            length = int(row["Length"])
            status = row["Status"]

            print("\nFiber ID:", fiber_id)
            print("Length:", length, "Meters")
            print("Length in KM:", length / 1000)
            print("Status:", status)


write_fiber_csv()
read_fiber_csv()
