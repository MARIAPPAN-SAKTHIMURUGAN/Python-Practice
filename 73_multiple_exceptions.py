def fiber_analysis(fiber):

    try:
        fiber_id = fiber["fiber_id"]
        length = int(fiber["length"])
        cores = int(fiber["cores"])

        print("Fiber ID:", fiber_id)
        print("Length KM:", length / 1000)
        print("Length per core:", length / cores)

    except KeyError:
        print("Required field is missing")

    except ValueError:
        print("Length and cores must be numbers")

    except ZeroDivisionError:
        print("Cores cannot be zero")


fiber = {
    "fiber_id": "F001",
    "length": "5000",
    "cores": "24"
}

fiber_analysis(fiber)
