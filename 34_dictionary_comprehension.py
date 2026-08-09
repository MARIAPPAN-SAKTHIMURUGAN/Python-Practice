def fiber_length():
    fibers = {
        "F001": 250,
        "F002": 450,
        "F003": 600,
        "F004": 800,
        "F005": 950
    }

    # Dictionary comprehension using items()
    result = {
        fiber: length * 1000
        for fiber, length in fibers.items()
    }

    # List comprehension using keys()
    result1 = [
        fiber
        for fiber in fibers.keys()
    ]

    # List comprehension using values()
    result2 = [
        length * 1000
        for length in fibers.values()
    ]

    print("Using items():", result)
    print("Using keys():", result1)
    print("Using values():", result2)


fiber_length()
