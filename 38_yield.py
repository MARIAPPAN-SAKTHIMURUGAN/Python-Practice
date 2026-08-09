def fiber_lengths():
    fibers = [250, 450, 600, 800, 950]

    for length in fibers:
        yield length * 1000


result = fiber_lengths()

for length in result:
    print("Fiber length:", length)
