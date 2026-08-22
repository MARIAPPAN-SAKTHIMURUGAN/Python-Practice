import json


def write_fiber_json():

    fibers = [
        {
            "fiber_id": "F001",
            "length": 450,
            "status": "Active"
        },
        {
            "fiber_id": "F002",
            "length": 950,
            "status": "Dark"
        },
        {
            "fiber_id": "F003",
            "length": 780,
            "status": "IPL"
        },
        {
            "fiber_id": "F004",
            "length": 1200,
            "status": "Active"
        }
    ]

    with open("fiber_data.json", "w") as file:

        json.dump(fibers, file, indent=4)

    print("Fiber JSON file created successfully.")


def read_fiber_json():

    with open("fiber_data.json", "r") as file:

        fibers = json.load(file)

    print("\n--- Fiber JSON Data ---")

    for fiber in fibers:

        print("\nFiber ID:", fiber["fiber_id"])
        print("Length:", fiber["length"], "Meters")
        print("Length in KM:", fiber["length"] / 1000)
        print("Status:", fiber["status"])


write_fiber_json()
read_fiber_json()
