def fiber_set():
    fibers = [
        "F001",
        "F002",
        "F001",
        "F003",
        "F002",
        "F004"
    ]

    result = {fiber for fiber in fibers}

    print("Original Fiber IDs:", fibers)
    print("Unique Fiber IDs:", result)


fiber_set()
